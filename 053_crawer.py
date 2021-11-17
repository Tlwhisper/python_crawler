# 爬虫 基础
import urllib.request
response = urllib.request.urlopen("http://www.baidu.com")
data = response.read()  # 这里read()没有参数,是这个对象的内置方法
data = data.decode("utf-8") # 使用utf-8解码
print(data)
