class Solution:
    def jumpFloor(self , number: int) -> int:
        # write code here
        dp=[0 for i in range(number+1)]
        dp[0]=1
        dp[1]=1
        dp[2]=2
        if number==1:
            print(1)
        elif number==2:
            print(2)
        else:
            for i in range(3,number+1):
                dp[i]=dp[i-1]+dp[i-2]
            print(dp[number])

hh=Solution()
hh.jumpFloor(2)
