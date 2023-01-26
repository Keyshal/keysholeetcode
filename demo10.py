#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param array int整型一维数组 
# @return int整型
#
class Solution:
    def FindGreatestSumOfSubArray(self , array: List[int]) -> int:
        # write code here


        # nums=[-2,-8,-1,-5,-9]
        nums=array
        lenn = len(nums)
        if lenn>1:
            dp = [0 for i in range(lenn)]
            dp[0]=nums[0]
            for i in range(1,lenn):
                dp[i] = max(dp[i-1]+nums[i], nums[i],)
            
            return max(dp)
        elif lenn==1:
            hh=max(nums)
            return max(nums)
        else:
            return 0
