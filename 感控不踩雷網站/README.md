# 臺大醫院感染管制中心｜感控不踩雷學習網站發布包

> **把感染管制做成直覺，妳/你就是病房裡最優雅的守護神。**  
> 用最專業的底氣，讓臨床工作游刃有餘。

---

## 📁 資料夾檔案說明

本資料夾已完整獨立打包，不依賴外部伺服器或後端資料庫，點擊即可本機運行，亦可直接整包上傳發布至 GitHub Pages！

| 檔案名稱 | 說明 | 適用對象 |
| :--- | :--- | :--- |
| **`presentation.html`** | **感控核心雜誌風簡報**（跑馬燈、5大單元卡片牆、全螢幕投影片播放，免密碼直接看） | 全體同仁課前/臨床自我研讀 |
| **`index.html`** | **主要學習對決首頁**（3D 粒子背景、三步驟身分切換、實戰對決與證書頒發） | 全體病房同仁（護理師、醫師、清潔人員、其他醫事同仁） |
| **`learning.html`** | 學習網備用連結（內容與 `index.html` 相同） | 全體同仁 |
| **`admin.html`** | **病房主管成果看板**（總人數、合格率、易錯排行榜、作答明細、Excel 匯出） | 護理長、感管醫師、主管同仁 |
| **`assets/`** | 網站所需之頭像、吉祥物與圖片素材 | 系統資源 |

---

## 🚀 本機快速開啟與體驗

1. **同仁闖關學習**：在電腦中對 **`index.html`** 點兩下，即可在瀏覽器（Edge / Chrome）開啟。
2. **主管成效監控**：對 **`admin.html`** 點兩下即可開啟。內建「🧪 注入範例測試數據」按鈕，可一鍵載入示範名單預覽圖表成效與 Excel 匯出。

---

## 🌐 發布至 GitHub Pages 教學（免費公開網址）

若要讓全病房同仁用自己的手機、平板或護理推車隨時作答：

1. **建立 GitHub 儲存庫（Repository）**：
   - 到 [GitHub](https://github.com/) 點選 **New repository**。
   - 名稱可取為 `ntuh-ic-guardian`，設為 **Public**。
2. **上傳此資料夾內的所有檔案**：
   - 將本資料夾內的 `index.html`、`learning.html`、`admin.html` 與 `assets/` 資料夾整批上傳至該 Repository 的根目錄。
3. **啟用 GitHub Pages**：
   - 進入該 Repository 的 **Settings** ➔ 左側選單 **Pages**。
   - 在 **Build and deployment** 下的 **Branch** 選擇 `main`，資料夾選擇 `/ (root)`，點擊 **Save**。
4. **取得發布網址**：
   - 約 1 分鐘後重新整理頁面，即可獲得專屬網址：  
     `https://<你的GitHub帳號>.github.io/ntuh-ic-guardian/`

---

## ☁️ 跨裝置雲端同步設定（Google 試算表 Webhook）

由於 GitHub Pages 為靜態託管，若希望同仁各自在手機填答完畢後，紀錄能自動即時彙整到主管的一份 Google 試算表中：

1. 開啟一份新的 **Google 試算表**。
2. 點選選單 **「擴充功能」➔「Apps Script」**。
3. 貼上以下 10 行腳本：

```javascript
function doPost(e) {
  var sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  var data = JSON.parse(e.postData.contents);
  sheet.appendRow([
    new Date(), 
    data.name, 
    data.role, 
    data.score, 
    data.passed ? '合格' : '待加強', 
    data.mistakesCount, 
    data.serial
  ]);
  return ContentService.createTextOutput(JSON.stringify({status:'ok'}))
    .setMimeType(ContentService.MimeType.JSON);
}
```

4. 點擊右上角 **「部署」➔「新增部署作業」➔ 選擇「網頁應用程式」**：
   - 誰可以存取：設為 **任何人 (Anyone)**。
5. 將獲得的 `https://script.google.com/macros/s/.../exec` 網址，複製貼進 **`admin.html`** 的「☁️ 雲端同步設定」中即可完成全自動雲端連線！
