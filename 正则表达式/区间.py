import re

m = re.search(r'[A-Za-z0-9]', 'A10.3')
print(m)                # 匹配

m = re.search(r'[0-25-7]', 'A3489C')
print(m)                # 不匹配
