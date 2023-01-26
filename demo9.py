class Solution:
    def LIS(self , arr: List[int]) -> int:
        # nums = [6, 3, 1, 5, 2, 3, 7]
        nums=arr
        lenn = len(nums)
        if lenn>0:
            dp = [1 for i in range(lenn + 1)]
            maxr = nums[0]
            for i in range(lenn):
                tmp1 = nums[i]
                for j in range(i):
                    tmp2 = nums[j]
                    if tmp1 > tmp2:
                        dp[i] = max(dp[i], dp[j] + 1)
            return max(dp)
        else:
            return 0
