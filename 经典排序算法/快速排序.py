# 快速排序
from typing import List

nums: List[int] = []
print('快速排序（升序排序）')


def quick_sort(data):
    if len(data) >= 2:
        mid = data[len(data) // 2]
        left = []
        right = []
        data.remove(mid)
        for num in data:
            if num >= mid:
                right.append(num)
            else:
                left.append(num)
        return quick_sort(left) + [mid] + quick_sort(right)
    else:
        return data


while True:
    print('请输入你想排列的数字个数：')
    try:
        x = int(input())
        for i in range(x):
            a = int(input('请输入第' + str(i + 1) + '个整数：'))
            nums.append(a)
    except ValueError:
        print('输入错误，请重新输入：')

    print(quick_sort(nums))

    jud = input('您是否想要继续？(Y/N)')
    while jud != 'Y' and jud != 'N':
        jud = input('输入错误，请重新输入：')
    if jud == 'Y':
        nums.clear()
        continue
    else:
        print('再见！')
        break
