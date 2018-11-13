# coding:utf-8
import urllib2
import urllib


def send_request():
    i = 0
    keyword = raw_input('请输入查询关键字:')
    pn = raw_input('请输入起始页码:')
    pn1 = raw_input('请输入结束页码')
    # 固定网址
    base_url = 'http://tieba.baidu.com/f?'

    # 构建查询字典
    for pn3 in range(int(pn), int(pn1)+1):
        query_dict = {'kw': keyword, 'pn': (int(pn3)-1) * 50}

        # 通过urlencode方法,构建查询字符串
        query_str = urllib.urlencode(query_dict)
        full_url = base_url + query_str
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}
        request = urllib2.Request(full_url, headers=headers)
        response = urllib2.urlopen(request)
        h = response.read()
        i+=1
        with open('baidu_%s.html' % str(i), 'w') as f:
            f.write(h)



if __name__ == '__main__':

    send_request()

