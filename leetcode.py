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
    # ValidAnagram
    if sys.argv[1].isalpha() and camel_to_snake(sys.argv[1]) == item["arg"]:
        pass
    elif sys.argv[1].lower() not in item["title"].lower():
        continue
    if sys.argv[2].lower() == "":
        item["arg"] = f"https://leetcode.cn/problems/{item['arg']}/description/"
    else:
        item["arg"] = f"https://www.google.com.hk/search?&q=site:programmercarl.com+{item['title']}"
    item["icon"] = {}
    item["icon"]["path"] =  "icon.png"
    result.append(item)
alfredJSON = json.dumps({"items": result}, indent=2, ensure_ascii=False)
sys.stdout.write(alfredJSON)