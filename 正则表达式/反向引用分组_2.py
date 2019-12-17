import re

p = r'<([\w]+)>.*</\1>'         # 使用反向分组

m = re.search(p, '<a>abc</a>')
print(m)                        # 匹配
m = re.search(p, '<a>abc</b>')
print(m)                        # 不匹配
