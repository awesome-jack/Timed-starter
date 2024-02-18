from cache_cookies import cache_cookie_main
import requests  

global cache_cookie
cache_cookie=cache_cookie_main

def renzhen():

    headers = {  
        'GET': '/wx/wechat/index.jsp?openid=6A1F36C6E73BCC010FAE434A96A41D2F&operatorId=weixin',  
        'Host': 'hnydsd.189jxt.com:8089',  
        'Upgrade-Insecure-Requests': '1',  
        'User-Agent': 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/33.0.0.0 Mobile Safari/537.36 MicroMessenger/6.0.0.54_r849063.501 NetType/WIFI',  
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',  
        'Referer': 'http://hnydsd.189jxt.com:8089/wx/wechat/login.jsp',  
        'Accept-Encoding': 'gzip, deflate',  
        'Accept-Language': 'zh-CN,zh;q=0.9',  
        'Cookie': 'JSESSIONID='+cache_cookie,  
        'Connection': 'keep-alive'  
    }  
    
    cookies = {  
        'JSESSIONID': cache_cookie 
    }  
    
    response = requests.get('http://hnydsd.189jxt.com:8089/wx/wechat/index.jsp?openid=6A1F36C6E73BCC010FAE434A96A41D2F&operatorId=weixin', headers=headers, cookies=cookies)  
    
    #print(response.text)  # 输出服务器响应的文本内容
    print("运行正常",cache_cookie)



#print(cache_cookie)