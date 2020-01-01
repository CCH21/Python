score = int(input('请输入分数：'))
if score >= 90:
    grade = 'A'
elif score >= 60:
    grade = 'B'
else:
    grade = 'C'
print('%s' % grade)
