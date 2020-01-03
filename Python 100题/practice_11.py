def hammingWeight(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count


num = int(input())
print(hammingWeight(num))
