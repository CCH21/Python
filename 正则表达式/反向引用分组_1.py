import re

p = r'<([\w]+)>.*</([\w]+)>'

m = re.search(p, '<a>abc</a>')
print(m)                        # 匹配
m = re.search(p, '<a>abc</b>')
print(m)                        # 匹配
