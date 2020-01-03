count = 0
for nOne in range(1, 101):
    for nTwo in range(1, 51):
        for nFive in range(1, 21):
            if nOne + nTwo * 2 + nFive * 5 == 100:
                count += 1
                print('方法%-3d：1*%d+2*%d+5*%d=100' % (count, nOne, nTwo, nFive))
