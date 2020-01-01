from sys import stdout

for i in range(1, 10):
    for j in range(1, 10):
        if i >= j:
            stdout.write('{0}×{1}={2:<3d}'.format(j, i, i * j))
    stdout.write('\n')
