import sys
import json

data = open('result.json').read()
data = json.loads(data)
result=[]
for item in data:
    if sys.argv[1].lower() not in item["title"].lower(): 
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