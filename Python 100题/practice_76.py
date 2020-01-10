for num in range(10, 100):
    if num * 809 == num * 800 + num * 9:
        if 10 <= num * 8 < 100:
            if 100 <= num * 9 < 1000:
                print('%d\n%d' % (num, 809 * num))
