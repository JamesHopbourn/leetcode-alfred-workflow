import json

data = open('leetcode.json').read()
data = json.loads(data)
result = []

for item in data:
  result.append({
    "title": f"{item['frontendQuestionId']} {str(item['titleCn'])}",
    "subtitle": item["title"],
    "arg": item['titleSlug']
    })

text = json.dumps(result,ensure_ascii=False)
print(text)