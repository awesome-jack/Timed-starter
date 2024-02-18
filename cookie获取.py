import requests

def analysis():

    url='http://hnydsd.189jxt.com:8089/wx/app/api/user/searchBindHouseListForMoney'

    response=requests.get(url=url)

    cokie=response.cookies

    session_id = cokie['JSESSIONID'] 

    print(session_id)

    cookie_string=str(cokie)

    #print(cookie_string)

    global data

    data=cookie_string[38:70]

   # print(sessionId)

    return data




analysis()

"""
    print(type(cookie_string))
    print(type(cookie))
    #cookie=cookie[13:25]




    04CA7E0869808FD15DF50CBE16483C58
    EBF719F36E42682661B8D4FC544F69EA
    DC78FA489A9DBF4D141E0270C69CA548
    04CA7E0869808FD15DF50CBE16483C58

"""