#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# longest common substring
# @param str1 string字符串 the string
# @param str2 string字符串 the string
# @return string字符串
#
class Solution:
    def LCS(self , str1: str, str2: str) -> str:
        # write code here
        a = str1
        a = '0' + a
        a = [i for i in a]
        b = str2
        b = '0' + b
        b = [i for i in b]
        lena = len(a)
        lenb = len(b)
        lenr = lena + abs(lena - lenb)
        dp = [[0 for i in range(lenr)] for k in range(lenr)]
        # 子序列不需要在原序列中占用连续的位置。而最长公共子串（要求连续）和最长公共子序列是不同的。 [2]
        # dp[7][7]=98
        # dp[i][j]=max(f[i][j],f[i-1][j-1])
        ff = {}
        for i in range(1, lena):
            for j in range(1, lenb):
                if a[i] == b[j]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    ff[dp[i][j]] = [i, j]
                else:
                    dp[i][j] = 0

        lenff = len(ff)
        k = ff[lenff]
        i = k[0]
        j = k[1]
        res=""
        while dp[i][j] != 0 and i!=0 and j!=0:
            res=a[i]+res
            i = i - 1
            j = j - 1
        # tmplist.reverse()
        return res
