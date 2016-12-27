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

 
COOKIES={
    '_xsrf':r'820c3d4709c7a72f52949a64f5cef0aa',
    'z_c0':'Mi4wQUFBQTRic2pBQUFBUUlKWWtZOFBDeGNBQUFCaEFsVk42SEtKV0FEdGRIREFjTWxPR0N1dVhIcElaSXpSeG51ZkVR|1482810858|3a200ace1a0340f144f7264874a2d318119248ea'
}

#获取连接
url = 'https://www.zhihu.com/topic/20052088/followers'
#user_agent = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36'}
user_agent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A403 Safari/8536.25'
user_agent = {'User-Agent':user_agent}

data = {'offset':'80','start':'1467355107','_xsrf':'820c3d4709c7a72f52949a64f5cef0aa'}
#data = json.dumps(data)
data = urllib.parse.urlencode(data)
data = data.encode('utf-8') #编译   

COOKIES = dict(cookies_are='working')
html = requests.get(url=url,data=data,headers=user_agent,cookies=COOKIES) 
#写入文档
fp = open('try2.txt','w',encoding='utf-8')
fp.write(html.text)
fp.close()

'''
response = urllib.request.urlopen(request)
#解析json
result = json.loads(response.read().decode('utf-8'))
        
print (result['msg'])        
'''