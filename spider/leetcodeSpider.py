import json
import requests

url = "https://leetcode.cn/graphql/"

all = []
for i in range(31):
  payload = json.dumps({
    "query": "query problemsetQuestionList($categorySlug: String, $limit: Int, $skip: Int, $filters: QuestionListFilterInput) {\n problemsetQuestionList(\n categorySlug: $categorySlug\n limit: $limit\n skip: $skip\n filters: $filters\n ) {\n hasMore\n total\n questions {\n acRate\n difficulty\n freqBar\n frontendQuestionId\n isFavor\n paidOnly\n solutionNum\n status\n title\n titleCn\n titleSlug\n topicTags {\n name\n nameTranslated\n id\n slug\n }\n extra {\n hasVideoSolution\n topCompanyTags {\n imgUrl\n slug\n numSubscribed\n }\n }\n }\n }\n}\n ",
    "variables": {
      "categorySlug": "algorithms",
      "skip": i*100,
      "limit": 100,
      "filters": {}
    },
    "operationName": "problemsetQuestionList"
  })
  headers = {
    'Content-Type': 'application/json',
  }
  response = requests.request("POST", url, headers=headers, data=payload)
  all.extend(json.loads(response.text)['data']['problemsetQuestionList']['questions'])

result = []
for item in all:
  difficultyMap = {
    'EASY': '简单',
    'MEDIUM': '中等',
    'HARD': '较难'
  }
  data = {
    "titleUS": f"{item['frontendQuestionId']} {str(item['title'])}",
    "titleCN": f"{item['frontendQuestionId']} {str(item['titleCn'])}",
    "subtitleUS": f"{item['difficulty']}",
    "subtitleCN": f"{difficultyMap[item['difficulty']]} {item['title']}",
    "arg": item['titleSlug']
  }
  data['subtitleCN'] = '💰 ' + data['subtitleCN'] if item['paidOnly'] else data['subtitleCN']
  data['subtitleUS'] = '💰 ' + data['subtitleUS'] if item['paidOnly'] else data['subtitleUS']
  result.append(data)

data = open('../result.json', 'w')
data.write(json.dumps(result, indent=4, ensure_ascii=False))
data.close()