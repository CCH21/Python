def fun(_list):
    ret = []
    count = 0
    for i in range(len(_list)):
        if _list[i] != 0:
            ret.append(_list[i])
        else:
            count += 1
    for j in range(count):
        ret.append(0)
    return ret


nums = list(eval(input()))
print(fun(nums))
