import urllib.request

#response = urllib.request.urlopen("http://placekitten.com/g/500/600")
# urlopen 的参数可以是字符串地址，也可以是一个request对象
req = urllib.request.Request("http://placekitten.com/g/400/600") # 实例化一个Request的类--> 对象
response = urllib.request.urlopen(req) # 传给urlopen的是一个request对象,返回一个类文件(文件对象)
cat_img = response.read()

# response 这个对象除了read方法外，还有geturl()、info()方法、getcode()返回状态码方法

print("response.geturl(): ")
print(response.geturl())
print("response.info()")
print(response.info())
print("response.getcode()")
print(response.getcode())
with open('cat_400_600','wb') as f:
    f.write(cat_img)
