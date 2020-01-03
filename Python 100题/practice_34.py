num = int(input())
a = num // 10000
b = num % 10000 // 1000
c = num % 1000 // 100
d = num % 100 // 10
e = num % 10

if a != 0:
    print('5位数\n%d%d%d%d%d' % (e, d, c, b, a))
elif b != 0:
    print('4位数\n%d%d%d%d' % (e, d, c, b))
elif c != 0:
    print('3位数\n%d%d%d' % (e, d, c))
elif d != 0:
    print('2位数\n%d%d' % (e, d))
else:
    print('1位数\n%d' % e)
