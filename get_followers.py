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
    '_xsrf':r'bdf3346b3204c468fe75974b68c91e02',
    '_ga':r'GA1.2.984600732.1434259989',
    '_za':r'a2f29937-643a-4a4d-b12a-b46b93226d82', 
    'udid':r'"AIBAh0arnAmPToK2Gm3g2RtgArq8_xmenHw=|1457912704"',
    'd_c0':r'"ACBA3amOpAmPTmjAGBJoF_raNQKOEvdN6eY=|1458442074"',
    '_zap':r'a834383e-39ca-453e-b66d-db2a6ce159dd',
    '__utmt':r'1',
    'l_cap_id':r'"MDg3YTZkYWRjOWU2NDJmZDlkNGY4YjRkNjEzZGVmNTk=|1468982359|d011b41513791faa266707c9acff732939035722"',
    'q_c1':r'86ed8cdc6b0d45c0ae4b29d9193d727a|1468982359000|1468982359000',
    'cap_id':r'"YmEzNjc1NWNiNjI1NGQyMGE1NTU3NjVmNzUwZWQ0NjY=|1468982359|b725ab1586038065fceeebf884e73681b8eed072"',
    'login':r'"Y2UxN2E1OTdhYWVlNDNkNWIzY2Y0MTA4NDc2MmNjNGE=|1468982397|cf12e029db3df79e10f94c1155c743e255134bb9"',
    'n_c':r'1',
    '__utma':r'51854390.984600732.1434259989.1468982362.1468982362.1',
    '__utmb':r'51854390.14.9.1468982511837',
    '__utmc':r'51854390',
    '__utmz':r'51854390.1468982362.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
    '__utmv':r'51854390.010--|2=registration_date=20140109=1^3=entry_date=20160720=1'
}

#获取连接
url = 'https://www.zhihu.com/topic/20052088/followers'
#user_agent = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36'}
user_agent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A403 Safari/8536.25'
user_agent = {'User-Agent':user_agent}

data = {'offset':'80','start':'1467355107','_xsrf':'de90e26028858a3472cd8efef2efa7ad'}
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