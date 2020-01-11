def fun(string):
    if string[0] != string[1]:
        return 0
    for i in range(1, len(string) - 1):
        if string[i] != string[i + 1]:
            return i + 1
    else:
        return -1


string = input()
print(fun(string))
