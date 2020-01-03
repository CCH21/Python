def climbStairs(n):
    if n == 1:
        return 1
    fib = [1, 1, 2]
    for i in range(3, n + 1):
        _next = fib[i - 1] + fib[i - 2]
        fib.append(_next)
    return fib[n]


n = int(input('请输入楼梯台阶数：'))
print(climbStairs(n))
