#coding: utf-8

import urllib2
import urllib

def send_renren():
    url="http://www.renren.com/968678593/profile"
    headers = {
              "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
              "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
              "Cache-Control": "max-age=0",
              "Connection": "keep-alive",
              "Cookie": "anonymid=jogho9ch-a05tj8; depovince=GW; _r01_=1; JSESSIONID=abcDkpAKb9zadfOu31pCw; ick_login=612e1bad-4838-45c7-9ebb-7f54242f223d; t=140797391ce5ff11054808da729cfa1e3; societyguester=140797391ce5ff11054808da729cfa1e3; id=968678593; xnsid=f02671c1; jebecookies=6c2078af-454a-4af3-8a24-a9efbffc91bc|||||; ch_id=10016; wp_fold=0; _ga=GA1.2.518013046.1542159346; _gid=GA1.2.600294873.1542159346",
              "Host": "www.renren.com",
              "Referer": "http://zhibo.renren.com/top",
              "Upgrade-Insecure-Requests": "1",
              "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}
    request=urllib2.Request(url,headers=headers)
    response=urllib2.urlopen(request)
    with open('renren.html','w') as  f:
        f.write(response.read())


if __name__ == '__main__':
    send_renren()
