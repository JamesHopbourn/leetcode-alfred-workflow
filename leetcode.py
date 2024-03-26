import os
import re
import sys
import json

data = open('result.json').read()
data = json.loads(data)
result = []
for item in data:
    if sys.argv[1] not in item['titleCN'] and sys.argv[1].lower() not in item['titleUS'].lower():
        continue
    # lc 和 sxl 公共字段提取，遇到 lcm 关键词再覆盖
    item['icon'] = {'path': 'icon.png'}
    item['title'] = item['titleCN']
    item['subtitle'] = item['subtitleCN']
    keyword = os.environ['alfred_workflow_keyword'].lower()
    if keyword == 'lc':
        item['arg'] = f"https://leetcode.cn/problems/{item['arg']}/description/"
    elif keyword == 'lcm':
        item['arg'] = f"https://leetcode.com/problems/{item['arg']}/description/"
        item['title'] = item['titleUS']
        item['subtitle'] = item['subtitleUS']
    elif keyword == 'sxl':
        parts = item['titleCN'].split(' ')
        text = ''.join(parts[1:]).replace(' ', '')
        formatted_title = '{:0>4}.{}.html'.format(parts[0], text)
        item['arg'] = f"https://programmercarl.com/{formatted_title}"
    result.append(item)
alfredJSON = json.dumps({'items': result}, indent=2, ensure_ascii=False)
sys.stdout.write(alfredJSON)
