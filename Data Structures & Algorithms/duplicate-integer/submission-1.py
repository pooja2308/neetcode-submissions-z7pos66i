class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_val = set()
        for i in nums:
            unique_val.add(i)
        if len(unique_val) < len(nums):
            return True
        else:
            return False
            