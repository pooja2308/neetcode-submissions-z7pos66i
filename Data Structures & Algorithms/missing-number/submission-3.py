class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        x1 = 0
        x2 = 0
        n=len(nums)
        # XOR all elements in array
        for i in range(len(nums)):
            x1 = x1 ^ nums[i]
        # XOR all numbers from 1 to n
        for i in range(1, n + 1):
            x2 = x2 ^ i
        return x1 ^ x2
