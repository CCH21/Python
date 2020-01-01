for num in range(100, 1000):
    i = num // 100
    j = num % 100 // 10
    k = num % 10
    s = i ** 3 + j ** 3 + k ** 3
    if num == s:
        print('%d' % num)
