class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_val = set()
        for num in nums:
            if num not in unique_val:
                unique_val.add(num)
        if len(unique_val) < len(nums):
            return True
        else:
            return False

            