class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 1:
            return cost[0]
        if len(cost) == 2:
            return min(cost[0], cost[1])
        dp = [0, min(0, cost[0])]
        for idx in range(2, len(cost) + 1):
            dp.append(min(dp[idx-1]+cost[idx-1], dp[idx-2]+cost[idx-2]))
        return dp[-1]