class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        result = []
        # for num in nums:
        #     if num % 2 == 0:
        #         result.insert(0, num)
        #     else:
        #         result.append(num)
        # return result

        l , r = 0, len(nums) - 1
        while l < r:
            if nums[l] % 2 > nums[r] % 2:
                nums[l], nums[r] = nums[r], nums[l]
            if nums[l] % 2 == 0:
                l += 1
            elif nums[r] % 2 == 1:
                r -= 1
        return nums
