from sys import stdout

num = int(input('请输入金字塔塔底长度：'))
direction = input('请输入金字塔塔尖方向(w/a/s/d)：')
h = (num + 1) // 2

if direction == 'w':
    for i in range(1, h + 1):
        for j in range(1, num + 1):
            if (j > h - i) and (j < h + i):
                stdout.write('*')
            else:
                stdout.write(' ')
        stdout.write('\n')
        
elif direction == 'a':
    for i in range(1, num + 1):
        for j in range(1, h + 1):
            if (j > h - i) and (j > i - h):
                stdout.write('*')
            else:
                stdout.write(' ')
        stdout.write('\n')
        
elif direction == 's':
    for i in range(1, h + 1):
        for j in range(1, num + 1):
            if (j >= i) and (j <= num - i + 1):
                stdout.write('*')
            else:
                stdout.write(' ')
        stdout.write('\n')

elif direction == 'd':
    for i in range(1, num + 1):
        for j in range(1, h + 1):
            if (j <= i) and (j <= 2 * h - i):
                stdout.write('*')
            else:
                stdout.write(' ')
        stdout.write('\n')

else:
    print('Error! ')
