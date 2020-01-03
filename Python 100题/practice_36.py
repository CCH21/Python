letter = input('请输入首字母（大写）：')
if letter == 'S':
    letter = input('请输入第二个字母（小写）：')
    if letter == 'a':
        print('Saturday')
    elif letter == 'u':
        print('Sunday')
    else:
        print('输入错误！')
elif letter == 'M':
    print('Monday')
elif letter == 'T':
    letter = input('请输入第二个字母（小写）：')
    if letter == 'u':
        print('Tuesday')
    elif letter == 'h':
        print('Thursday')
    else:
        print('输入错误！')
elif letter == 'W':
    print('Wednesday')
elif letter == 'F':
    print('Friday')
else:
    print('输入错误！')
