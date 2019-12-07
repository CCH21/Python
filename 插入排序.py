# 插入排序
nums = []

print('插入排序（升序排序）')
while True:
    print('请输入你想排列的数字个数：')
    try:
        x = int(input())
        for i in range(x):
            a = int(input('请输入第' + str(i + 1) + '个整数：'))
            nums.append(a)
    except ValueError:
        print('输入错误，请重新输入：')

    for i in range(1, len(nums)):
        for j in range(i, 0, -1):
            if nums[j] < nums[j - 1]:
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
            else:
                break
    print(nums)

    jud = input('您是否想要继续？(Y/N)')
    while jud != 'Y' and jud != 'N':
        jud = input('输入错误，请重新输入：')
    if jud == 'Y':
        nums.clear()
        continue
    else:
        print('再见！')
        break
