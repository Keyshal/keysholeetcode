#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param m int整型 
# @param n int整型 
# @return int整型
#
class Solution:
    def uniquePaths(self , m: int, n: int) -> int:
        # m = 1
        # n = 2
        dp = [[0 for i in range(n + 1)] for j in range(m + 1)]
        dp[0][0] = 1
        for i in range(0, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        res = dp[m - 1][n]
        return res
        # print("haha")
