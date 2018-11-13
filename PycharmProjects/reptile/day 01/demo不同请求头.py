# coding:utf-8
import random
import urllib2

USER_AGENT_LIST = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6"
]


def send_request():
    useragent = random.choice(USER_AGENT_LIST)
    request = urllib2.Request('http://www.baidu.com/')
    request.add_header('User-Agent', useragent)
    response = urllib2.urlopen(request)
    if response.getcode() == 200:
        html = response.read()
        return html
    return None


if __name__ == '__main__':
    html = send_request()
    if html:
        with open('baidu.html', 'w') as f:
            f.write(html)
