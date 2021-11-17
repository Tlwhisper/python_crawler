# 正则表达式
# . 通配符，除了换行之外的任意字符
# \.
# \d 通配符任意数字
import re
print(re.search(r'\d','I love Fish.c1122334455'))

# 字符类 [ ]
# 匹配其中的任何一个都算
print(re.search(r'[aeiou]','I love fishc.com'))

# - 表示范围
print(re.search(r'[1-9]','I love 012546fishc.com'))

# {}表示匹配的次数
print(re.search(r'ab{3}c','abbbc'))
# {}匹配次数的 范围
print(re.search(r'ab{1,3}c','abbc'))

# 匹配0-255之间的数字
print(re.search(r'[01]\d\d|2[0-4]\d|25[0-4]','188'))

# 匹配ip地址
print(re.search(r'(([01]\d\d|2[0-4]\d|25[0-4])\.){3}[01]\d\d|2[0-4]\d|25[0-4]','192.168.120.188'))

# 匹配192.168.0.1, 不满3位
print(re.search(r'(([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-4])\.){3}[01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-4]','192.168.0.1'))



print(re.search(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$","1.1.1.251"))
