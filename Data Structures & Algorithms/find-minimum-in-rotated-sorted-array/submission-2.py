class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) -1
        
        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                
            # first check the mid of nums
            m = (l + r) // 2
            res = min(res, nums[m])

            # check if mid is greater than left most value 
            # that means min value is at next to mid position else mid minus 1
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return res
            