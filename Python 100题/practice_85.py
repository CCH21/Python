nums = [1, 2, 3, 4, 1, 3, 2, 4, 5, 7, 7, 6, 6]
for i in range(len(nums)):
    if nums.count(nums[i]) == 1:
        print('nums[%d]: %d' % (i, nums[i]))
        break
