str1 = input()
str2 = input()
dp = []
for i in range(len(str1)):
    dp.append([])
    for j in range(len(str1)):
        dp[i].append(0)
maxLen = 0
for i in range(len(str1)):
    for j in range(len(str2)):
        if str1[i] == str2[j]:
            if i == 0 or j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > maxLen:
                    maxLen = dp[i][j]
        else:
            dp[i][j] = 0
print(maxLen)
