# url的错误处理
import urllib.error
import urllib.request
'''
req = urllib.request.Request("http://xxoo-fishc.com")
try:
    urllib.request.urlopen(req)
except urllib.error.URLError as e:
    print(e.reason)  # [Errno -2] Name or service not known

'''
req = urllib.request.Request("http://www.fishC.com")
try:
    urllib.request.urlopen(req)
#except urllib.error.HTTPError as e:
    print(e.code)
    #print(e.read())



# 模板写法
'''
from urllib.request import Request, urlopen
from urllib.error import URLError
req = Request(someurl)

try:
    response = urlopen(req)
except URLError as e:
    if hasattr(e, 'reason'):
        print('We failed to reach a server.')
        print('Reason: ', e.reason)
    elif hasattr(e, 'code'):
        print('The server could\'t fulfill the request.')
        print('Error code: ', e.code)
else:
    #everything is fine





'''
