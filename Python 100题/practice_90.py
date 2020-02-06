def swap(s, i, j):
    t = s[i]
    s[i] = s[j]
    s[j] = t


def permutation(s, start):      # 对字符串中的字符进行全排列
    if s is None or start < 0:
        return

    # 完成全排队后输出当前排列的字符串
    if start == len(s) - 1:
        print("".join(s))
    else:
        i = start
        while i < len(s):
            swap(s, start, i)               # 交换start与i所在位置的字符
            permutation(s, start + 1)       # 固定第一个字符，对其余字符进行全排列
            swap(s, start, i)               # 还原start与i所在的位置的字符
            i += 1


s = input()
s = list(s)
permutation(s, 0)
