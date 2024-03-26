import json
import requests

url = "https://leetcode.cn/graphql/"

problemset = []
for i in range(31):
  payload = json.dumps({
    "query": "query problemsetQuestionList($categorySlug: String, $limit: Int, $skip: Int, $filters: QuestionListFilterInput) {problemsetQuestionList(categorySlug: $categorySlug limit: $limit skip: $skip filters: $filters ) {hasMore total questions {difficulty frontendQuestionId paidOnly title titleCn titleSlug }}} ",
    "variables": {
      "categorySlug": "algorithms",
      "skip": i*100,
      "limit": 100
    },
    "operationName": "problemsetQuestionList"
  })
  response = requests.request("POST", url, headers={'Content-Type': 'application/json'}, data=payload)
  problemset.extend(json.loads(response.text)['data']['problemsetQuestionList']['questions'])

result = []
difficulty = {'EASY': '简单', 'MEDIUM': '中等', 'HARD': '较难'}
for item in problemset:
  data = {
    "arg": item['titleSlug'],
    "titleUS": f"{item['frontendQuestionId']} {str(item['title'])}",
    "titleCN": f"{item['frontendQuestionId']} {str(item['titleCn'])}",
    "subtitleUS": f"{item['difficulty'].title()}",
    "subtitleCN": f"{difficulty[item['difficulty']]} {item['title']}"
  }
  data['subtitleCN'] = '💰 ' + data['subtitleCN'] if item['paidOnly'] else data['subtitleCN']
  data['subtitleUS'] = '💰 ' + data['subtitleUS'] if item['paidOnly'] else data['subtitleUS']
  result.append(data)

data = open('result.json', 'w')
data.write(json.dumps(result, indent=4, ensure_ascii=False))
data.close()