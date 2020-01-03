from sys import stdout

a = []
for i in range(10):
    a.append([])
    for j in range(10):
        a[i].append(0)
for i in range(0, 10):
    for m in range(0, 10 - i):
        stdout.write("  ")
    for j in range(0, i + 1):
        if (j == 0) or (i == j):
            a[i][j] = 1
        else:
            a[i][j] = a[i - 1][j - 1] + a[i - 1][j]
        stdout.write('%4d' % (a[i][j]))
    stdout.write("\n")
