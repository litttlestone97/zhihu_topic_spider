import requests,time
from bs4 import BeautifulSoup
import urllib
import urllib.parse
import urllib.error
import urllib.request
from openpyxl import load_workbook
from openpyxl import Workbook 

def get_captcha(data):
    with open('captcha.gif','wb') as fp:
        fp.write(data)
    return input('输入验证码：')
 
def login(username,password,oncaptcha):
    sessiona = requests.Session()
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'}
    _xsrf = BeautifulSoup(sessiona.get('https://www.zhihu.com/#signin',headers=headers).content,'html.parser').find('input',attrs={'name':'_xsrf'}).get('value')
    captcha_content = sessiona.get('https://www.zhihu.com/captcha.gif?r=%d&type=login'%(time.time()*1000),headers=headers).content
    data = {
        "_xsrf":_xsrf,
        "email":username,
        "password":password,
        "remember_me":True,
        "captcha":oncaptcha(captcha_content)
    }
    resp = sessiona.post('https://www.zhihu.com/login/email',data,headers=headers).content
    print(resp)
    return sessiona 
 
if __name__ == "__main__":
    user_name = input("请输入用户名：")
    password = input("请输入密码：")
    sessiona=login(user_name,password,get_captcha)
    
    #获取连接
    url = 'https://www.zhihu.com/topic/20052088/followers'
    #user_agent = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36'}
    user_agent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A403 Safari/8536.25'
    user_agent = {'User-Agent':user_agent}

    data = {'offset':'80','start':'1466787246','_xsrf':'820c3d4709c7a72f52949a64f5cef0aa'}
    #data = json.dumps(data)
    data = urllib.parse.urlencode(data)
    data = data.encode('utf-8') #编译   

    html = sessiona.get(url=url,data=data,headers=user_agent) 
    #写入文档
    fp = open('try2.txt','w',encoding='utf-8')
    fp.write(html.text)
    fp.close()