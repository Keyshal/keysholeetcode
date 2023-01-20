#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# longest common subsequence
# @param s1 string字符串 the string
# @param s2 string字符串 the string
# @return string字符串
#
class Solution:
    def LCS(self , s1: str, s2: str) -> str:
        a = s1
        b = s2
        a = "0"+a
        a = [i for i in a]
        b = "0"+b
        b = [i for i in b]
        lena = len(a)
        lenb = len(b)
        lenr = lena + abs(lena - lenb)
        dp = [[0 for i in range(lenr)] for k in range(lenr)]
        # 子序列不需要在原序列中占用连续的位置。而最长公共子串（要求连续）和最长公共子序列是不同的。 [2]
        # dp[7][7]=98
        # dp[i][j]=max(f[i][j],f[i-1][j-1])
        for i in range(1, lena):
            for j in range(1, lenb):
                if a[i] == b[j]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    # tmplist.append(dp[i][j])
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                    # dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1] + (a[i] == b[j]))
        i = lena - 1
        j = lenb - 1
        tmplist1 = []
        while i != 0 and j != 0:
            f1 = a[i]
            f2 = b[j]
            # print(f1, "-", f2)
            if a[i] == b[j]:
                tmplist1.append(a[i])
                i = i - 1
                j = j - 1

            elif dp[i - 1][j] > dp[i][j - 1]:
                i = i - 1

            elif dp[i][j - 1] > dp[i - 1][j]:
                j = j - 1

            else:
                i = i - 1
        tmplist1.reverse()
        res = ""
        for i in tmplist1:
            res = res + i
        # res.rjust()
        # print("haha")
        if res=="":
            return "-1"
        return res
