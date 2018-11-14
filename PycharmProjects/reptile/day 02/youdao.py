# coding:utf-8
import hashlib
import json
import random
import time
import urllib
import urllib2


def get_token():
    text=raw_input('请输入文本:')
    salt=str(int(time.time()*1000)+random.randint(0,10))
    sign = hashlib.md5("fanyideskweb" + text + salt + "sr_3(QOHT)L2dx#uuGR@r").hexdigest()
    return (text,salt,sign)



def send_requ():
    url='http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    header = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Connection": "keep-alive",
        "Content-Length": "218",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Cookie": "OUTFOX_SEARCH_USER_ID=169386323@59.111.179.142; OUTFOX_SEARCH_USER_ID_NCOO=2081201158.7946014; _ntes_nnid=501941341babfd75e977d6b05a01a28a,1535100680645; _ga=GA1.2.304145068.1535448983; LAST_LOGIN=zl_8876@163.com; JSESSIONID=aaakg7-QCwXvLd54ymmCw; ___rl__test__cookies=1542097859964",
        "Host": "fanyi.youdao.com",
        "Origin": "http://fanyi.youdao.com",
        "Referer": "http://fanyi.youdao.com/?keyfrom=fanyi.logo",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"}

    text,salt,sign =get_token()

    form_dict = {
        "i": text,
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": salt,
        "sign": sign,
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_CLICKBUTTION",
        "typoResult": "false",
    }
    form_str=urllib.urlencode(form_dict)
    header['Content-Length']=len(form_str)
    request =urllib2.Request(url,form_str,header)
    response=urllib2.urlopen(request)

    #将需要打印的结果转为python数据类型
    json_data =json.loads(response.read())
    #获取结果
    trans_text = json_data["translateResult"][0][0]["tgt"]
    print(trans_text)

if __name__ == '__main__':
    send_requ()

























# ++++++++++++++++++++++++++
'''
1 有道有加密

2 hashlib 用来产生msd5 和sha1
    hashlib.md5('字符串')=====> 会产生MD5的一个对象
    hashlib.md5('字符串').hexdigest()===>产生一个加密的md5值(短一些)
    
  s1=hashlib.sha1()=======>首先要产生一个对象
  s1.update('字符串')
  s1.hexdigest()======>产生一个加密的sha1值(长一些)
    



'''
