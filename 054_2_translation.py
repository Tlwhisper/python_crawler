# json 轻量级的数据交换格式
# python中的有内口格式 和 json格式类似
# 用字符串的形式把python的数据结构给封装起来，就是json格式

# python中数据 默认是 由内扣 的格式，UTF-8是 由内扣的一种编码格式

# 有内扣格式---> utf-8编码 ： data = urllib.parse.urlencode(data).encode('utf-8') ： 字符串格式-->有内口格式 --->  utf-8格式
# utf-8格式 ---> 有内口文件格式：html = response.read().decode('utf-8')

# Form Data 就是我们提交的表单数据
# F12 唤出：审阅，输入翻译文字，点击NetWork,在name右键：把method给唤出来。
# 找到post方法，找到url地址，找到表单信息，封装成data数据。

import urllib.request
import urllib.parse
import json
contend = input("请输入需要翻译的内容:")

#url = 'https://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
url = 'https://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
data = {} # 封装数据


data['i'] = contend
data['from']= 'AUTO'
data['to'] = 'AUTO'
data['smartresult'] = 'dict'
data['client'] =  'fanyideskweb'
data['salt'] =  '16370343749742'
#data['sign'] =  '3139464d0f92968d800dfce171ec5c44'  # 可写 可不写
#data['lts'] =  '1637034374974'
#data['bv'] =  'c795a332c678d5063a1ee5eb15253848'
data['doctype'] =  'json'
data['version'] = '2.1'
data['keyfrom'] =  'fanyi.web'
data['action'] =  'FY_BY_CLICKBUTTION'

data = urllib.parse.urlencode(data).encode('utf-8') # 使用这个函数把字符串转乘utf-8格式

response = urllib.request.urlopen(url, data)
html = response.read().decode('utf-8')

target = json.loads(html)  # load最后一个s，表示string



# 请输入需要翻译的内容:帅哥
print(target)
# {'type': 'ZH_CN2EN', 'errorCode': 0, 'elapsedTime': 10, 'translateResult': [[{'src': '帅哥', 'tgt': 'The handsome boy'}]]}

print(target['translateResult'])
# [[{'src': '帅哥', 'tgt': 'The handsome boy'}]]

print(target['translateResult'][0])
# [{'src': '帅哥', 'tgt': 'The handsome boy'}]

print(target['translateResult'][0][0]) 
# {'src': '帅哥', 'tgt': 'The handsome boy'}


print("翻译结果：%s" % (target['translateResult'][0][0]['tgt']))


# 翻译结果：The handsome boy

