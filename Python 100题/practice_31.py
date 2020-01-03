def fact(j):
    s = 0
    if j == 1:
        s = 1
    else:
        s = j * fact(j - 1)
    return s


print(fact(5))
