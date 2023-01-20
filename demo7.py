#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 解码
# @param nums string字符串 数字串
# @return int整型
#
class Solution:
    def solve(self, nums: str) -> int:        
        # nums="100"
        lennum = len(nums)
        dp = [0] * (lennum + 1)
        dp[0] = 1
        if lennum >= 1:
            dp[1] = 1
            if nums=="0":
                return 0
           
        i=2
        while i <= lennum:
            tmp1 = nums[i - 2:i]
            tmp2 = nums[i - 1:i]
            
            if int(tmp1) > 26 or int(tmp1)<=10:
                dp[i] = dp[i - 1]
            else:
                dp[i] = dp[i - 1] + dp[i - 2]
            i = i + 1
        if nums[-1]=='0' and i>3:
            return 0
        return dp[lennum]
