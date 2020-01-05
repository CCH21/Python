def fun(n):
    s = 0
    if n & 1 == 0:
        for i in range(2, n + 1, 2):
            s += 1 / i
    else:
        for i in range(1, n + 1, 2):
            s += 1 / i
    return s


n = int(input())
print(fun(n))
