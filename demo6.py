#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param matrix int整型二维数组 the matrix
# @return int整型
#
class Solution:
    def minPathSum(self , matrix: List[List[int]]) -> int:
        # matrix = [[1, 2, 3], [1, 2, 3]]

        lenm = len(matrix)
        lenn = len(matrix[0])
        dp = [[0 for i in range(lenn + 1)] for k in range(lenm + 1)]
        count = matrix[0][0]
        dp[0][0] = count
        for i in range(1, lenn):
            count = count + matrix[0][i]
            dp[0][i] = count

        count = matrix[0][0]
        for j in range(1, lenm):
            count = count + matrix[j][0]
            dp[j][0] = count

        for i in range(1, lenm):
            for j in range(1, lenn):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + matrix[i][j]
        hh = dp[lenm - 1][lenn - 1]
        return hh
