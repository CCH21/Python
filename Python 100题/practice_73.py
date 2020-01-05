nums = [2, 7, 11, 15]
target = int(input())
for i in range(4):
    for j in range(i + 1, 4):
        if nums[i] == target - nums[j]:
            print(i, j)
