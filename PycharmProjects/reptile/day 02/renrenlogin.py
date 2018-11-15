# coding: utf-8
import cookielib
import urllib
import urllib2


def send_request():
    post_url = 'http://www.renren.com/PLogin.do'
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}
    form_dict = {
        "email": "mr_mao_hacker@163.com",
        "password": "ALARMCHIME"
    }
    form_data = urllib.urlencode(form_dict)
    request = urllib2.Request(post_url, form_data, headers)
    # 1 构建一个可以储存cookie的cookiejar对象
    cookie_jar = cookielib.CookieJar()
    # 2. 使用cookiejar对象，构建可以处理cookie的处理器对象
    cookie_handler = urllib2.HTTPCookieProcessor(cookie_jar)
    # 3.使用处理器对象，构建opener
    opener = urllib2.build_opener(cookie_handler)
    response = opener.open(request)
    with open('renrenlogin.html', 'w') as f:
        f.write(response.read())


if __name__ == '__main__':
    send_request()
