again = 1
while again:
    num = int(input())
    print(num**2)
    if num**2 >= 50:
        again = 1
    else:
        again = 0
