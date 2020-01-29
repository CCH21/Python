def fun(_list, n):
    if n <= 2:
        return _list[n - 1]
    else:
        i = n % 3
        m = n // 3
        for j in range(m, 0, -1):
            _list.remove(_list[3 * j - 1])
            listNext = _list[-i:] + _list[:-i]
        return fun(listNext, n - m)


n = int(input())
peopleList = list(range(1, n + 1))
print(fun(peopleList, n))
