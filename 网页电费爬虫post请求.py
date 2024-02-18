import requests  
from cookie认证 import renzhen,cache_cookie



def start():

    headers = {  
        'POST': '/wx/app/api/user/searchBindHouseListForMoney',  
        'Host': 'hnydsd.189jxt.com:8089',  
        'Accept': 'application/json, text/javascript, */*; q=0.01',  
        'X-Requested-With': 'XMLHttpRequest',  
        'User-Agent': 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/33.0.0.0 Mobile Safari/537.36 MicroMessenger/6.0.0.54_r849063.501 NetType/WIFI',  
        'Origin': 'http://hnydsd.189jxt.com:8089',  
        'Referer': 'http://hnydsd.189jxt.com:8089/wx/wechat/houseMeterSurplus.jsp?openid=6A1F36C6E73BCC010FAE434A96A41D2F&metersort=3',  
        'Accept-Encoding': 'gzip, deflate',  
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',  
        'Cookie': 'JSESSIONID='+cache_cookie,  
        'Connection': 'keep-alive',  
        'Content-Length': '37',  
        'Content-Type': 'application/x-www-form-urlencoded'  
    }  
    
    cookies = {  
        'JSESSIONID':cache_cookie 
    }  
    #944F175694C1F318FC840A56D727FCAE
    form_data = {  
        'wxId': '6A1F36C6E73BCC010FAE434A96A41D2F'  
    }  
    
    response = requests.post('http://hnydsd.189jxt.com:8089/wx/app/api/user/searchBindHouseListForMoney', headers=headers, cookies=cookies, data=form_data)  
    
    print(response.text)  # 输出服务器响应的文本内容
    print("二次验证",cache_cookie)


def total():
    renzhen()
    start()

total()