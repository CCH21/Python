nums = list(eval(input()))
k = int(input())
n = len(nums)
result = []
for i in range(n - k, n):
    result.append(nums[i])
for i in range(n - k):
    result.append(nums[i])
print(result)
