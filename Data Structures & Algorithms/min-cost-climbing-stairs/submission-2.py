class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # # bottom up/tabulation approach
        # Time complexity = O(n)
        # Space Complexity = O(n)

        # n = len(cost)
        # dp = [0] * (n+1)
        
        # # so the base cases are that at index 0 or 1 there is no cost and 
        # # as we are already setting everything to 0, no need to define it explicitly
        # for i in range(2, n+1):
        #     dp[i] = min(dp[i-2] + cost[i-2], dp[i-1] + cost[i-1])
        # return dp[-1] or dp[n]

        # bottom up/tabulation approach with constant space
        # Time complexity = O(n)
        # Space Complexity = O(1)

        n = len(cost)
        prev, cur = 0, 0
        
        for i in range(2, n+1):
            prev, cur = cur, min(cost[i-2] + prev, cost[i-1] + cur)
        return cur
        