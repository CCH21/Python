def hanoi(n, a, b, c):
    if n == 1:
        print(a, '->', c)
        return
    hanoi(n - 1, a, c, b)
    print(a, '->', c)
    hanoi(n - 1, b, a, c)


num = int(input('请输入圆盘数量：'))
print('移动方法如下：')
hanoi(num, 'A', 'B', 'C')
