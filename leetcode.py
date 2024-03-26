import os
import re
import sys
import json

data = open('result.json').read()
data = json.loads(data)
result = []
for item in data:
    if sys.argv[1] not in item["titleCN"] and sys.argv[1].lower() not in item["titleUS"].lower():
        continue
    item["icon"] = {}
    item["icon"]["path"] =  "icon.png"
    if os.environ['alfred_workflow_keyword'].lower() == "lc":
        item["arg"] = f"https://leetcode.cn/problems/{item['arg']}/description/"
        item['title'] = item['titleCN']
        item['subtitle'] = item['subtitleCN']
        result.append(item)
    elif os.environ['alfred_workflow_keyword'].lower() == "lcm":
        item["arg"] = f"https://leetcode.com/problems/{item['arg']}/description/"
        item['title'] = item['titleUS']
        item['subtitle'] = item['subtitleUS']
        result.append(item)
    elif os.environ['alfred_workflow_keyword'].lower() == "sxl":
        parts = item['titleCN'].split(' ')
        text = ''.join(parts[1:]).replace(' ', '')
        formatted_title = '{:0>4}.{}.html'.format(parts[0], text)
        item["arg"] = f"https://programmercarl.com/{formatted_title}"
        result.append(item)
alfredJSON = json.dumps({"items": result}, indent=2, ensure_ascii=False)
sys.stdout.write(alfredJSON)
