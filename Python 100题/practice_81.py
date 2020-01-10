num = int(input('请输入加密前的四位数字：'))
a = num // 1000
b = num % 1000 // 100
c = num % 100 // 10
d = num % 10
a = (a + 5) % 10
b = (b + 5) % 10
c = (c + 5) % 10
d = (d + 5) % 10
a, d = d, a
b, c = c, b
print('加密后的数字为：%d%d%d%d' % (a, b, c, d))
