def fun(nums):
    return len(list(set(nums))) != len(nums)


nums = list(eval(input()))
print(fun(nums))
