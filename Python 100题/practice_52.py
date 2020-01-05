a = int(input())
b = a >> 4
c = ~(~0 << 4)
d = b & c
print('%o\t%o' % (a, d))
