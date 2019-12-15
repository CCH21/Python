ch = input()
k = int(input())
a = 'abcdefghijklmnopqrstuvwxyz'
A = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in ch:
    if 'a' <= i <= 'z':
        n = a.find(i)
        print(a[(n + k + 26) % 26], end='')
    elif 'A' <= i <= 'Z':
        n = A.find(i)
        print(A[(n + k + 26) % 26], end='')
    else:
        print(i, end='')
