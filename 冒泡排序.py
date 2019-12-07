# 冒泡排序
nums = []

print('冒泡排序（升序排序）')
while True:
    print('请输入你想排列的数字个数：')
    try:
        x = int(input())
        for i in range(x):
            a = int(input('请输入第' + str(i + 1) + '个整数：'))
            nums.append(a)
    except ValueError:
        print('输入错误，请重新输入：')

    for j in range(len(nums) - 1):
        for k in range(len(nums) - j - 1):
            if nums[k] > nums[k + 1]:
                nums[k], nums[k + 1] = nums[k + 1], nums[k]
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
