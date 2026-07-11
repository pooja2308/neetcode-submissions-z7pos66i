class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        non_zero = 0
        for num in range(len(nums)):
            if nums[num] != 0:
                nums[non_zero], nums[num] = nums[num], nums[non_zero]
                non_zero += 1
    

