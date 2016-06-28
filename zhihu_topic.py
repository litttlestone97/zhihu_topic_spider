#-*- coding:utf-8 -*-
import zhihu_more
#加载话题18*j,覆盖加载
j = 0
for i in range(0,1):	#每次修改i的区间
	i+=1
	zhihu_more.zhihu_topic_more(j)
	j+=19
print ('over')

