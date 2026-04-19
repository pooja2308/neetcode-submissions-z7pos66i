class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))
        


    def helper(self, nums):
        n = len(nums)
        d = [0] * (n-1)
        prev = 0
        cur = 0

        for num in nums:
            prev, cur = cur, max(cur, num + prev)
        return cur
        
        

        