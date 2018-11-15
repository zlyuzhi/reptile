#coding: utf-8


import urllib2

def send_request():
    # 构建特定处理器对象
    http_handle=urllib2.HTTPHandler()
    #构建带有处理器功能的opener对象
    opener=urllib2.build_opener(http_handle)
    #使用opener对象open()发送请求
    response =opener.open('https://www.baidu.com')
    print(response.read())


if __name__ == '__main__':
    send_request()