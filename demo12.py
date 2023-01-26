#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param str1 string字符串 
# @param str2 string字符串 
# @return int整型
#
class Solution:
    def editDistance(self , str1: str, str2: str) -> int:
        # write code here
        m, n = len(str1), len(str2)
        dp = [[0] * (n+1) for _ in range(m+1)] # 状态转移方程 (m, n) matrix
        # 初始化边界
        for i in range(m+1):
            dp[i][0] = i 
        for j in range(n+1):
            dp[0][j] = j
        for i in range(1, m+1):
            for j in range(1, n+1):
                if str1[i-1] == str2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])+1
        return dp[m][n]
