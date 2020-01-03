def fibo(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)


month = int(input('请输入月份数：'))
print('兔子总数为%d只' % (2 * fibo(month)))
