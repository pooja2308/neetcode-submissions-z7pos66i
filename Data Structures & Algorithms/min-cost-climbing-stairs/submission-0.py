class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # bpttom up/tabulation approach

        n = len(cost)
        dp = [0] * (n+1)
        
        # so the base cases are that at index 0 or 1 there is no cost and 
        # as we are already setting everything to 0, no need to define it explicitly
        for i in range(2, n+1):
            dp[i] = min(dp[i-2] + cost[i-2], dp[i-1] + cost[i-1])
        print(dp)
        return dp[-1]
        