# coding:utf-8
import json
import urllib
import urllib2

'''
抓取豆瓣电影类型
    特点
    get请求,有ajax
    需要通过往下拉翻页才能获取更多页面,所以要用到循环不断抓取

准备工作
    1 获取url地址,通过抓包获取
    2 获取请求报文头
    3 构建查询字串

代码书写方法
    在死循环的结构下
        1 构建完整的url地址(url+请求参数)
        2 构建请求对象
            请求对象来自urlib2.Request这个类
            请求对象的参数是(完整的url,请求头)
        3 发送请求
            发送请求的方法是urllib2.urlopen()
            发送的参数是请求对象
        3 读取url响应
        4 转换类型,非空跳出循环

'''


def send_request():
    base_url = 'https://movie.douban.com/j/chart/top_list?type=17&interval_id=100%3A90&action=&'
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}

    start = 0
    while True:

        query_dict = {'start': start, 'limit': '50'}
        query_str = urllib.urlencode(query_dict)
        url = base_url + query_str
        request = urllib2.Request(url, headers=headers)
        response = urllib2.urlopen(request)

        json_str = response.read()

        if not json.loads(json_str):
            break

        douban = json_str
        with open('douban.txt', 'w') as f:
            print('[INFO]:正在保存数据 {}...' '.format(豆瓣)')
            f.write(douban)

        start += 20


if __name__ == '__main__':
    send_request()


#怎么在pycharm里面使用正则处理爬下来的数据
# \{\"
# \t\{\"
# 怎么在写的过程加入日志
# print("[INFO] : 正在保存数据 {}..".format(file_name))
