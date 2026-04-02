class Solution:
    def findMin(self, nums: List[int]) -> int:
            res = nums[0]
            l, r = 0 , len(nums) - 1
            # first check the mid of nums
            while l <= r:
                if nums[l] < nums[r]:
                    res = min(nums[l], res)
                    break

                mid = (l + r) // 2
                res = min(nums[mid], res)
            
                # check if mid is greater than left most value 
                # that means min value is at next to mid position else mid minus 1
                # if nums[mid] >= nums[l] and nums[l] >= nums[r]:
                if nums[mid] >= nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            return res


            