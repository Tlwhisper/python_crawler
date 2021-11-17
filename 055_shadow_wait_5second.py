
import urllib.request
import urllib.parse
import json
import time
while True:
    contend = input("请输入需要翻译的内容(输入!q 推出程序):")
    if contend =='!q':
        break
    url = 'https://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'

    '''
    # 方式 1
    head = {}
    head['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
    '''


    data = {} # 封装数据
        
    data['i'] = contend
    data['from']= 'AUTO'
    data['to'] = 'AUTO'
    data['smartresult'] = 'dict'
    data['client'] =  'fanyideskweb'
    data['salt'] =  '16370343749742'
    data['doctype'] =  'json'
    data['version'] = '2.1'
    data['keyfrom'] =  'fanyi.web'
    data['action'] =  'FY_BY_CLICKBUTTION'

    data = urllib.parse.urlencode(data).encode('utf-8') # 使用这个函数把字符串转乘utf-8格式

    #req = urllib.request.Request(url, data,head)
    req = urllib.request.Request(url, data)

    # 方式2，动态的追加
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36')


    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')

    target = json.loads(html)  # load最后一个s，表示string

    print("head is %s" % (req.headers))

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
    time.sleep(5)

    # 翻译结果：The handsome boy

