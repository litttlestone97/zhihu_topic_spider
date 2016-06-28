#-*- coding:utf-8 -*-
#练习抓取虎嗅网数据
import urllib
import urllib.parse
import urllib.error
import urllib.request
import json
import re
url = 'http://www.huxiu.com/v2_action/article_list'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
#data = {'huxiu_hash_code':'322cf76eec54c4e275d7c8122028a3b2','page':8}
data = {'page':8}
data = urllib.parse.urlencode(data)
data = data.encode('utf-8') #编译   
try:
    request = urllib.request.Request(url=url,data=data) 
    response = urllib.request.urlopen(request)

    #解析json
    result = json.loads(response.read().decode('utf-8'))
    
    print (result['msg'])
    content = result['data']
    #匹配文章标题
    
    pattern = re.compile('<div class="mob-ctt">.*?target="_blank">(.*?)</a>',re.S)
    #虎嗅文章标题
    items = re.findall(pattern,content)
    for item in items:
        print (item)
except urllib.error.URLError as e:
    if hasattr(e,"code"):
        print (e.code)
    if hasattr(e,"reason"):
        print (e.reason)