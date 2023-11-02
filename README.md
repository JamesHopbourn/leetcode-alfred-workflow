# leetcode-alfred-workflow
Leetcode 题目搜素 Alfred Workflow

### 使用方法
#### lc 题目信息
搜索题目，并在 Leetcode 打开
![](image/bilibili.png)

#### sxl 题目信息
搜素题目，配合谷歌 site 高级搜索，在代码随想录查找题解文章
![](image/google.png)

### 思路
1. 爬虫抓取所有题目
```shell
python leetcodeSpider.py > leetcode.json
```
2. 清洗数据
```shell
python processJSON.py > result.json
```