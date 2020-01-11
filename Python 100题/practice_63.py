nums = list(eval(input()))
m = int(input())
n = len(nums)
result = []
for i in range(n - m, n):
    result.append(nums[i])
for i in range(n - m):
    result.append(nums[i])
print(result)
