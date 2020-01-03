def fun(n):
    if n == 1:
        return True
    while n > 3 and n % 3 == 0:
        n /= 3
    if n == 3:
        return True
    else:
        return False


num = int(input())
print(fun(num))
