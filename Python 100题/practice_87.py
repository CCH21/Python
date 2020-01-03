list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
_dict = {}
for i in range(len(list1)):
    _dict[list1[i]] = list2[i]
print(_dict)
