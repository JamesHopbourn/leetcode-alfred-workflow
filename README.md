# leetcode-alfred-workflow
Leetcode 题目搜素

#### 思路
1. 爬虫抓取所有题目
```shell
python leetcodeSpider.py > leetcode.json
```
2. 清洗数据
```shell
python processJSON.py > result.json
```