# coding:utf-8
import json
import random
import time
import urllib2
import urllib


def qq_translate():
    url="https://fanyi.qq.com/api/translate"
    headers={"Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Connection": "keep-alive",
    "Content-Length": "265",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Cookie": "pgv_pvi=9564194816; pgv_pvid=8030531696; RK=3Gz0HOqFYq; ptcz=fc597d6f115ee2ef4928037dc79591bc9d8b8c3cace67f204255cdf1b32babc0; pt2gguin=o0846145368; o_cookie=846145368; pac_uid=1_846145368; ptui_loginuin=846145368; fy_guid=4634545a-30f4-46af-9c60-bc48504af873; pgv_info=ssid=s9345781795; ts_refer=www.so.com/s; ts_uid=4354593300; gr_user_id=a693c9c9-cde8-4ecf-a2a7-b773d47d4cb4; grwng_uid=a24df833-3d7c-4fbe-ba70-56a156e274ef; qtv=65c8c95ce9760c44; qtk=L3SyRLqjrVyWUuZBX8jMA8JhLYbsp/2SfMXkbH26+myLxdrIZLySXMcsUfRCAYzmqR6wYgy65SLUKNm5Mw6U23VQJPYly5nkp8OMK6sGmrdKCRGcCF67hlnHDIb0Jr4+51hHj/tteD0D5fMGShmLLQ==; ts_last=fanyi.qq.com/; openCount=3; 9c118ce09a6fa3f4_gr_session_id=8197be1e-f095-47d6-8bea-661c73ddf471; 9c118ce09a6fa3f4_gr_session_id_8197be1e-f095-47d6-8bea-661c73ddf471=true",
    "Host": "fanyi.qq.com",
    "Origin": "https://fanyi.qq.com",
    "Referer": "https://fanyi.qq.com/",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"}

    # 构建表单
    form_dict={"source": "auto",
    "target": "auto",
    "sourceText": raw_input('请输入要翻译的内容:'),
    "qtv": "65c8c95ce9760c44",
    "qtk": "L3SyRLqjrVyWUuZBX8jMA8JhLYbsp/2SfMXkbH26+myLxdrIZLySXMcsUfRCAYzmqR6wYgy65SLUKNm5Mw6U23VQJPYly5nkp8OMK6sGmrdKCRGcCF67hlnHDIb0Jr4+51hHj/tteD0D5fMGShmLLQ==",
    "sessionUuid": "translate_uuid"+str(int(time.time())*1000)}
    form_str =urllib.urlencode(form_dict)

    #请求文本的长度应该和表单的长度一样
    headers['Content-Length'] = len(form_str)

    request =urllib2.Request(url,form_str,headers)
    response = urllib2.urlopen(request)
    # 将json字符串转为对应的Python数据类型
    python_dict=json.loads(response.read())
    #取结果
    answer =python_dict['translate']["records"][0]['targetText']
    print(answer)















if __name__ == '__main__':

    qq_translate()




# ++++++++++++++++++++++++++++++++++++++++++++
'''
1 uuid 打算怎么产生
time.time()就会产生一个uuid

2 表单的数据长度是不是一个注意点
请求文本的长度应该和表单的长度一样
    headers['Content-Length'] = len(form_str)


3 字典里的值怎么取
[0]是因为取里面列表的第一个





'''




