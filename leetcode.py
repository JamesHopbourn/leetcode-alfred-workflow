import os
import re
import sys
import json

def camel_to_snake(camel_case_string):
    snake_case_string = re.sub(r'([A-Z])', r'-\1', camel_case_string)
    return snake_case_string.lstrip('-').lower()

data = open('result.json').read()
data = json.loads(data)
result = []
for item in data:
    if sys.argv[1].isalpha() and camel_to_snake(sys.argv[1]) in item["arg"]:
        pass
    elif sys.argv[1].lower() not in item["title"].lower():
        continue
    if os.environ['alfred_workflow_keyword'].lower() == "lc":
        item["arg"] = f"https://leetcode.cn/problems/{item['arg']}/description/"
    else:
        parts = item['title'].split(' ')
        text = ''.join(parts[1:]).replace(' ', '')
        formatted_title = '{:0>4}.{}.html'.format(parts[0], text)
        item["arg"] = f"https://programmercarl.com/{formatted_title}"
    item["icon"] = {}
    item["icon"]["path"] =  "icon.png"
    result.append(item)
alfredJSON = json.dumps({"items": result}, indent=2, ensure_ascii=False)
sys.stdout.write(alfredJSON)
