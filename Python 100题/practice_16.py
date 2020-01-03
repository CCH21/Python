n = int(input('请输入一个正整数：'))
print('%d=' % n, end='')
for i in range(2, n + 1):
    while n != i:
        if n % i == 0:
            print('%d*' % i, end='')
            n /= i
        else:
            break
print('%d' % n)
