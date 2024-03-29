import os
import re
import sys
import json

data = open('result.json').read()
data = json.loads(data)

text = ' '.join(sys.argv[1:])
text = '.*' + '.*'.join(text.split()) + '.*'

result = []
for item in data:
    # 匹配中文或者英文标题
    if not re.search(text.lower(), item['titleCN'] + item['titleUS'].lower()):
        continue
    # lc 和 sxl 公共字段提取，遇到 lcm 关键词再覆盖
    item['icon'] = {'path': 'icon.png'}
    item['title'], item['subtitle'] = item['titleCN'], item['subtitleCN']
    # lc 和 sxl 公共字段提取，遇到 lcm 关键词再覆盖
    item['icon'] = {'path': 'icon.png'}
    item['title'], item['subtitle'] = item['titleCN'], item['subtitleCN']
    keyword = os.environ['alfred_workflow_keyword'].lower()
    if keyword == 'lc':
        item['arg'] = f"https://leetcode.cn/problems/{item['arg']}/description/"
    if keyword == 'lcm':
        item['arg'] = f"https://leetcode.com/problems/{item['arg']}/description/"
        item['title'], item['subtitle'] = item['titleUS'], item['subtitleUS']
    if keyword == 'sxl':
        parts = item['titleCN'].split(' ')
        text = ''.join(parts[1:]).replace(' ', '')
        formatted_title = '{:0>4}.{}.html'.format(parts[0], text)
        item['arg'] = f"https://programmercarl.com/{formatted_title}"
    result.append(item)
alfredJSON = json.dumps({'items': result}, indent=2, ensure_ascii=False)
sys.stdout.write(alfredJSON)
