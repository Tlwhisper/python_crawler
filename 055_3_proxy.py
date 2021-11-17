# 这个文件不好用，搞成代理模式,就是跑不出来


import urllib.request
import random

#url = 'http://www.whatismyip.com.tw'
url = 'http://www.baidu.com'

iplist =['119.6.144.73:81', '183.203.208.166:8118', '111.1.32.28:81']

#proxy_support = urllib.request.ProxyHandler({'http':'119.6.73.81'})
# 随机选一个ip，
proxy_support = urllib.request.ProxyHandler({'http':random.choice(iplist)})

opener = urllib.request.build_opener(proxy_support)
opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36')]

urllib.request.install_opener(opener)

response = urllib.request.urlopen(url)

html = response.read().decode('utf-8')

print(html)
