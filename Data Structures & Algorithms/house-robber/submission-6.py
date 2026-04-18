class Solution:
    def rob(self, nums: List[int]) -> int:
        # bottom up approach
        # Time complexity = O(n)
        # Space Complexity = O(n)
        # n = len(nums)
        
        # if not nums:
        #     return 0
        # if len(nums) == 1:
        #     return nums[0]
        # if len(nums) == 2:
        #     return max(nums[0], nums[1])
        # dp = [0] * n
        # dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        # for i in range(2, n):
        #     dp[i] = max(dp[i-1],  dp[i-2] + nums[i])
        # return dp[n-1] or dp[-1] 


        # bottom up approach with constant space complexity
        # Time complexity = O(n)
        # Space Complexity = O(1)
        n = len(nums)
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        prev, cur = nums[0], max(nums[0], nums[1])
        for i in range(2, n):
            prev, cur = cur, max(cur,  nums[i] + prev)
        return cur