num = int(input('请输入一个五位数：'))
a = num // 10000
b = num % 10000 // 1000
c = num % 1000 // 100
d = num % 100 // 10
e = num % 10
if a == e and b == d:
    print('%d是回文数' % num)
else:
    print('%d不是回文数' % num)
