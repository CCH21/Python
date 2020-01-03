import random

tmp = ''
for i in range(4):
    n = random.randrange(0, 2)          # 生成随机数1或0，用来判断下面，是生成随机数字，还是字母
    if n == 0:
        num = random.randrange(65, 91)  # 随机数为0时，生成大写字母
        tmp += chr(num)
    else:
        k = random.randrange(0, 10)     # 随机数为1时，生成数字
        tmp += str(k)
print(tmp)
