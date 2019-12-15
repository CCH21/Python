import re

p = r'[Jj]ava'

m = re.search(p, 'I like Java and Python.')
print(m)                # 匹配

m = re.search(p, 'I like JAVA and Python.')
print(m)                # 不匹配

m = re.search(p, 'I like java and Python.')
print(m)                # 匹配
