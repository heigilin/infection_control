with open('感控不踩雷網站/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Find sec-line block
start_line_marker = '<!-- 臨床口袋神隊友：台大感管 LINE 官方帳號 (@ntuhic) -->'
end_line_marker = '      <div class="learn-cards-grid">'

start_pos = html.find(start_line_marker)
end_pos = html.find(end_line_marker)

print("start_pos of line block:", start_pos)
print("end_pos of line block:", end_pos)

if start_pos != -1 and end_pos != -1:
    line_block = html[start_pos:end_pos].strip()
    html_without_line = html[:start_pos] + html[end_pos:]
    
    # Now find where sec-quiz ends
    # sec-quiz contains </section> and <aside class="profile panel">...</aside>\n    </div>
    aside_end = html_without_line.find('</aside>\n    </div>')
    if aside_end == -1:
        aside_end = html_without_line.find('</aside>\r\n    </div>')
    
    print("aside_end found:", aside_end)
    if aside_end != -1:
        insert_pos = aside_end + len('</aside>\n    </div>')
        new_html = html_without_line[:insert_pos] + '\n\n    <!-- ===== 第四階段：LINE 官方帳號口袋書 ===== -->\n    ' + line_block + '\n' + html_without_line[insert_pos:]
        
        with open('感控不踩雷網站/index.html', 'w', encoding='utf-8') as f:
            f.write(new_html)
        print("Reordered sec-line after sec-quiz successfully!")
