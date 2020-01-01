year = int(input('Year:'))
month = int(input('Month:'))
day = int(input('Day:'))
flag = 0
if (year % 400 == 0) or (year % 4 == 0) and (year % 100 != 0):
    flag = 1
months = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334)
if 0 < month <= 12:
    s = months[month - 1]
else:
    print('输入错误')
s += day
if (flag == 1) and (month > 2):
    s += 1
print('这是这一年的第%d天' % s)
