#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param A string字符串
# @return int整型
#
class Solution:
    def getLongestPalindrome(self , A: str) -> int:
        # write code here
        # nums = "ababc"
        nums=A
        lenn = len(nums)
        dp = [0 for i in range(lenn + 1)]
        for i in range(1, lenn + 1):
            for j in range(0, i):
                tmp = nums[j:i]
                if tmp[::-1] == tmp:
                    hh = len(tmp)
                    dp[i] = max(dp[i], hh)

        return max(dp)
