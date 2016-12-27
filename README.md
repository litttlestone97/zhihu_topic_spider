zhihu_topic_spider
####写作目的
+ 抓取知乎话题
+ 分析关注话题的用户数
+ 手动筛选感兴趣的话题
+ 分析最活跃用户，获得活跃用户清单
+ 抽查活跃用户的贡献是否有价值
+ 交叉比较活跃用户的关注点
+ 分析活跃用户的价值观，关注点，基本信息等

####日期
+ 计划开始：2016-06-20
+ 计划结束：2016-08-01（anyway）
+ 20161227

####说明
+ 仅用于python抓包的学习


####环境
+ python3.5

####功能模块

######function.py     存储函数
+ topic_more        抓取后面18条话题
+ topic_all         根据输入链接，更新话题描述，话题关注人数 

######主程序
+ get_topic.py     循环获取知乎子话题(topic_more)
+ get_main_topic.py 抓取知乎主话题,单页
+ get_topic_from_root.py      通过节点关系，从根节点发散获取话题(未开始)
+ get_topic_all      刷新子话题信息(topic_all)
+ get_followers      获取话题关注人列表


---
2.53.6 selenium


---
https://www.zhihu.com/topics