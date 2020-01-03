_dict = {'a': 1, 'b': 4, 'c': 2, 'd': 12}
print(_dict)
_dict = dict(sorted(_dict.items(), key=lambda x: x[1]))
print(_dict)
