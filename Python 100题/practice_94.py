def fun(n):
    if n == 0:
        return 1
    else:
        return fun(n-1) * 2


print(fun(20))
