def age(n):
    if n == 1:
        a = 10
    else:
        a = age(n - 1) + 2
    return a


print(age(5))
