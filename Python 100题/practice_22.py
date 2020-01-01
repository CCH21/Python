Tn = 0
Sn = []
n = int(input('n = '))
a = int(input('a = '))
for b in range(n):
    Tn = Tn + a
    a = a * 10
    Sn.append(Tn)
print('sum =', sum(Sn))
