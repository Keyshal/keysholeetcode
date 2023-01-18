class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # cost = [2, 5, 20]
        target = len(cost)
        dp = [0 for i in range(target + 1)]
        # for i in range():
        dp[0] = 0
        dp[1] = 0
        # dp[2] = 5
        for i in range(2, target + 1):
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
        return dp[target]
