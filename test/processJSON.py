import json

data = open('leetcode.json').read()
data = json.loads(data)
result = []

for item in data:
  difficultyMap = {
    'EASY': '简单',
    'MEDIUM': '中等',
    'HARD': '较难'
  }
  data = {
    "title": f"{item['frontendQuestionId']} {str(item['titleCn'])}",
    "subtitle": f"{difficultyMap[item['difficulty']]} {item['title']}",
    "arg": item['titleSlug']
  }
  if item['paidOnly']:
    data['subtitle'] = '💰 ' + data['subtitle']
  result.append(data)

text = json.dumps(result,ensure_ascii=False)
print(text)