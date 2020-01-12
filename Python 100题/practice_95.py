n = int(input())
list1 = [i for i in range(n + 1)]
list2 = list(eval(input()))
list3 = []
for j in range(len(list1)):
    if list1[j] not in list2:
        list3.append(list1[j])
print(list3)
