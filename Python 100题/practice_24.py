tour = []
height = []
hei = 100
time = 10
for i in range(1, time + 1):
    if i == 1:
        tour.append(hei)
    else:
        tour.append(2 * hei)
    hei /= 2
    height.append(hei)
print('总高度：tour = %f' % sum(tour))
print('第10次反弹高度：height = %f' % height[-1])
