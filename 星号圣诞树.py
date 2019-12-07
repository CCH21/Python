def main():
    from sys import stdout

    for i in range(1, 6):
        stdout.write(' ' * (20-2*i) + '\033[1;32m*\033[0m' * (4*i-3))
        stdout.write('\n')
    for i in range(6, 11):
        stdout.write(' ' * (25-2*i) + '\033[1;34m*\033[0m' * (4*i-13))
        stdout.write('\n')
    for i in range(11, 16):
        stdout.write(' ' * (30-2*i) + '\033[1;36m*\033[0m' * (4*i-23))
        stdout.write('\n')
    for i in range(16, 24):
        stdout.write(' ' * 15 + '\033[1;31m*\033[0m' * 7)
        stdout.write('\n')


if __name__ == '__main__':
    main()
