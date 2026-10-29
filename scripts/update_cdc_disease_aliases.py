from __future__ import annotations

import json
import re
import urllib.request
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[1]
OUT_FILE = BASE_DIR / "gas_line_bot" / "cdc_disease_aliases.json"
DISEASE_URL = "https://www.cdc.gov.tw/Disease/"
GLOSSARY_URL = "https://www.cdc.gov.tw/Category/Page/H7QkJbw4MlQX3u1Akf5AYw"


class DiseaseLinkParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.in_link = False
        self.href = ""
        self.buf: list[str] = []
        self.items: list[dict[str, str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag.lower() != "a":
            return
        href = dict(attrs).get("href") or ""
        if "/Disease/SubIndex/" not in href:
            return
        self.in_link = True
        self.href = href
        self.buf = []

    def handle_data(self, data: str) -> None:
        if self.in_link:
            self.buf.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() != "a" or not self.in_link:
            return
        self.in_link = False
        name = tidy_text("".join(self.buf))
        if name and not name.startswith("Image:"):
            self.items.append({"name": name, "href": self.href})


class TableCellParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.in_td = False
        self.buf: list[str] = []
        self.cells: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag.lower() == "td":
            self.in_td = True
            self.buf = []

    def handle_data(self, data: str) -> None:
        if self.in_td:
            self.buf.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() != "td" or not self.in_td:
            return
        self.in_td = False
        text = tidy_text("".join(self.buf))
        if text:
            self.cells.append(text)


def fetch(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "ntuh-ic-line-bot-alias-builder/1.0"})
    with urllib.request.urlopen(req, timeout=30) as response:
        encoding = response.headers.get_content_charset() or "utf-8"
        return response.read().decode(encoding, errors="replace")


def tidy_text(text: str) -> str:
    return re.sub(r"\s+", " ", text.replace("\ufeff", "")).strip()


def clean_disease_name(text: str) -> str:
    return re.sub(r"^[ㄅ-ㄩ]\s*", "", tidy_text(text))


def normalize_zh(text: str) -> str:
    table = str.maketrans("ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ１２３４５６７８９０ｂ", "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890b")
    return re.sub(r"[\s()（）/／、,，]", "", text.translate(table)).lower()


def add_alias(aliases: dict[str, list[str]], disease: str, value: str) -> None:
    value = tidy_text(value)
    if not value or value == disease:
        return
    bucket = aliases.setdefault(disease, [])
    if value not in bucket:
        bucket.append(value)


def base_terms(name: str) -> list[str]:
    terms = [name]
    for part in re.split(r"[/／、]", name):
        part = tidy_text(part)
        if len(part) >= 2:
            terms.append(part)
    paren = re.findall(r"[（(]([^）)]+)[）)]", name)
    terms.extend(tidy_text(p) for p in paren if tidy_text(p))
    return terms


def english_variants(term: str) -> list[str]:
    terms = [term]
    for part in re.split(r",|;|；|/| or ", term):
        part = tidy_text(part)
        if len(part) >= 2:
            terms.append(part)
    for acronym in re.findall(r"\(([A-Za-z0-9 -]{2,12})\)", term):
        terms.append(tidy_text(acronym))
    cleaned = tidy_text(re.sub(r"\([^)]*\)", "", term))
    if cleaned:
        terms.append(cleaned)
    return terms


def find_disease_for_zh(zh: str, diseases: list[str]) -> str:
    n = normalize_zh(zh)
    for disease in diseases:
        if normalize_zh(disease) == n:
            return disease
    for disease in diseases:
        dn = normalize_zh(disease)
        if n and (n in dn or dn in n):
            return disease
    return ""


def main() -> None:
    disease_parser = DiseaseLinkParser()
    disease_parser.feed(fetch(DISEASE_URL))
    diseases: list[str] = []
    disease_links: dict[str, str] = {}
    for item in disease_parser.items:
        name = clean_disease_name(item["name"])
        if name not in disease_links:
            diseases.append(name)
            disease_links[name] = item["href"]

    aliases: dict[str, list[str]] = {}
    for disease in diseases:
        aliases.setdefault(disease, [])
        for term in base_terms(disease):
            add_alias(aliases, disease, term)

    glossary_parser = TableCellParser()
    glossary_parser.feed(fetch(GLOSSARY_URL))
    cells = glossary_parser.cells
    for idx in range(0, len(cells) - 1, 2):
        english = cells[idx]
        chinese = cells[idx + 1]
        disease = find_disease_for_zh(chinese, diseases)
        if not disease:
            continue
        for term in english_variants(english):
            add_alias(aliases, disease, term)

    manual = {
        "人類免疫缺乏病毒(愛滋病毒)感染": ["HIV", "AIDS", "愛滋", "愛滋病毒", "人類免疫缺乏病毒"],
        "小兒麻痺症/急性無力肢體麻痺": ["AFP", "acute flaccid paralysis", "acute flaccid myelitis", "polio", "poliomyelitis", "小兒麻痺", "小兒麻痺症"],
        "中東呼吸症候群冠狀病毒感染症": ["MERS", "MERS-CoV"],
        "嚴重急性呼吸道症候群": ["SARS"],
        "新型A型流感": ["novel influenza A", "H5N1", "H7N9", "avian influenza", "禽流感"],
        "流感併發重症": ["influenza", "severe complicated influenza", "flu"],
        "新冠併發重症": ["COVID-19", "COVID", "SARS-CoV-2", "coronavirus disease 2019", "新冠"],
        "M痘": ["mpox", "monkeypox"],
        "發熱伴血小板減少綜合症": ["SFTS", "severe fever with thrombocytopenia syndrome"],
        "侵襲性b型嗜血桿菌感染症": ["Hib", "Haemophilus influenzae type b"],
        "侵襲性肺炎鏈球菌感染症": ["IPD", "invasive pneumococcal disease"],
        "多重抗藥性結核病": ["MDR-TB", "MDR TB"],
        "腸道出血性大腸桿菌感染症": ["EHEC", "enterohemorrhagic E. coli"],
        "庫賈氏病": ["CJD", "Creutzfeldt-Jakob disease", "prion disease"],
    }
    for disease, terms in manual.items():
        if disease not in aliases:
            aliases[disease] = []
        for term in terms:
            add_alias(aliases, disease, term)

    payload = {
        "version": 1,
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "sources": [
            {"title": "衛生福利部疾病管制署：傳染病介紹", "url": DISEASE_URL},
            {"title": "衛生福利部疾病管制署：雙語詞彙", "url": GLOSSARY_URL},
        ],
        "aliases": {key: aliases[key] for key in sorted(aliases)},
        "disease_links": {key: disease_links[key] for key in sorted(disease_links)},
    }
    OUT_FILE.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {OUT_FILE}")
    print(f"Diseases: {len(diseases)}")
    print(f"Alias groups: {len(payload['aliases'])}")


if __name__ == "__main__":
    main()
