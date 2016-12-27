#-*- coding:utf-8 -*-
#筛选话题之后，获取话题的关注者及相关信息

'''
功能描述：
+ 筛选感兴趣的话题   增加标志位
+ 话题关注者    know_man.xlsx	遍历完去重
+ 人员资料分析

编写日期：20160702
编写人：little_Stone
'''
 
import urllib
import urllib.parse
import urllib.error
import requests
import json
import re
#from bs4 import BeautifulSoup
import urllib.request
from openpyxl import load_workbook
from openpyxl import Workbook 
from function import * 

user_name = input("请输入用户名：")
password = input("请输入密码：")
sessiona=login(user_name,password,get_captcha)

topic='20052088'
start='1467008592'

#获取连接
url = 'https://www.zhihu.com/topic/'+topic+'/followers'
user_agent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A403 Safari/8536.25'
user_agent = {'User-Agent':user_agent}


#获取20条数据
data = {'offset':'100','start':start,'_xsrf':'820c3d4709c7a72f52949a64f5cef0aa'}
data = urllib.parse.urlencode(data)
data = data.encode('utf-8') #编译   
#html = sessiona.get(url=url,data=data,headers=user_agent)

#抽取此20条数据
try:
	request = urllib.request.Request(url=url,data=data) 
	response = urllib.request.urlopen(request)
    #解析json
	result = json.loads(response.read().decode('utf-8'))
    
	if number%100 ==0  :
		print ('正在写入第',number,'条数据')            
	content = result['msg']

	step=len(content)
    #print('step',step) #验证步长
    #匹配链接
    #循环取strong/href/p/ href="/topic/

	'''
    topic='<strong>(.*)</strong>'
    meaning='<p>(.*)</p>'
    href='href="(/topic/.*)">'

    href_list = re.compile('href="(/topic/.*)">')
    meaning_list = re.compile('<p>(.*)</p>')
    topic_list = re.compile('<strong>(.*)</strong>')
    '''

	#写入文档
	fp = open('try2.txt','w',encoding='utf-8')
	fp.write(content.text)
	fp.close()

except urllib.error.URLError as e:
	print (e.code)