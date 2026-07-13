class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_length = 0
        length = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                length += 1
                max_length = max(max_length, length)
            else:
                length = 0
        return max_length
                
        