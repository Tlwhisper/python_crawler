# 使用正则表达式获取 代理 ip
# 小甲鱼视频教程地址
#https://www.bilibili.com/video/BV1xs411Q799?p=61


import urllib.request
import re

def open_url(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36')
    page = urllib.request.urlopen(req)
    html = page.read().decode('utf-8')
    return html

def get_img(html):
    p = r'(?:(?:[0,1]?\d?\d|2[0-4]\d|25[0-5])\.){3}(?:[0,1]?\d?\d|2[0-4]\d|25[0-5])'
    iplist = re.findall(p, html)
    for each in iplist:
        print(each)


if __name__ == '__main__':
    #url = "http://cn-proxy.com"
    url = "https://ip.ihuan.em/address/5Lit5Zu9.html"
    get_img(open_url(url))

