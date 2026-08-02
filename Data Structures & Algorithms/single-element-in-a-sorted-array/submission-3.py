class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if mid % 2 == 1: # which means index is not even from the pair
                mid -= 1
            if nums[mid] == nums[mid + 1]: # perfect pair so move l 
            # to start of next pair
                l = mid + 2
            else:
                r = mid #single element could be mid or before mid
        return nums[r]
            
        