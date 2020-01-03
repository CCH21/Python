def output(s, length):
    if length == 0:
        return
    print(s[length - 1], end='')
    output(s, length - 1)


s = input()
length = len(s)
output(s, length)
