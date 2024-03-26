import requests
import json

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
    'Authorization': '',
    'Accept': '*/*',
    'Sec-Fetch-Site': 'same-origin',
    'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
    'Sec-Fetch-Mode': 'cors',
    'Accept-Encoding': 'gzip, deflate, br',
    'Origin': 'https://leetcode.cn',
    'Referer': 'https://leetcode.cn/problemset/algorithms/',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15',
    'Content-Length': '856',
    'Connection': 'keep-alive',
    'Host': 'leetcode.cn',
    'Cookie': 'csrftoken=S4tArKGPZJSbEwAEJd7h2ZjLabYHbPALb23De8uGjTi8CtyVpY45Vn1yLTT8PsGk; _ga_PDVPZYN3CW=GS1.1.1698763788.1.0.1698763798.50.0.0; Hm_lpvt_f0faad39bcf8471e3ab3ef70125152c3=1698763789; Hm_lvt_f0faad39bcf8471e3ab3ef70125152c3=1698763789; _ga=GA1.1.521235585.1698763788; _gat=1; _gid=GA1.2.1970910868.1698763788; a2873925c34ecbd2_gr_session_id=43bbd97a-bf58-40db-b3ed-f6fb9932c718; a2873925c34ecbd2_gr_session_id_sent_vst=43bbd97a-bf58-40db-b3ed-f6fb9932c718; gr_user_id=2982af0a-27cf-49b3-bc5b-e2e9754ed40b; csrftoken=S4tArKGPZJSbEwAEJd7h2ZjLabYHbPALb23De8uGjTi8CtyVpY45Vn1yLTT8PsGk',
    'Sec-Fetch-Dest': 'empty',
    'random-uuid': 'cd2ed977-c829-e8fc-213a-df6408f7627c',
    'x-csrftoken': 'S4tArKGPZJSbEwAEJd7h2ZjLabYHbPALb23De8uGjTi8CtyVpY45Vn1yLTT8PsGk',
    'baggage': 'sentry-environment=production,sentry-release=c609c887,sentry-transaction=%2Fproblemset%2F%5Bslug%5D,sentry-public_key=1595090ae2f831f9e65978be5851f865,sentry-trace_id=c23cb38428934dcfbb6ddb427ae0223f,sentry-sample_rate=0.03',
    'sentry-trace': 'c23cb38428934dcfbb6ddb427ae0223f-be7c75bdb635ef30-0'
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
    "title": f"{item['frontendQuestionId']} {str(item['titleCn'])}",
    "subtitle": f"{difficultyMap[item['difficulty']]} {item['title']}",
    "arg": item['titleSlug']
  }
  data['subtitle'] = '💰 ' + data['subtitle'] if item['paidOnly'] else data['subtitle']
  result.append(data)

data = open('../result.json', 'w')
data.write(json.dumps(result, indent=4, ensure_ascii=False))
data.close()