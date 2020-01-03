import string

s = input('请输入一个字符串：')
letters = 0
space = 0
digit = 0
others = 0
for c in s:
    if c.isalpha():
        letters += 1
    elif c.isspace():
        space += 1
    elif c.isdigit():
        digit += 1
    else:
        others += 1
print('字母：%d个，空格：%d个，数字：%d个，其他字符：%d个' % (letters, space, digit, others))
