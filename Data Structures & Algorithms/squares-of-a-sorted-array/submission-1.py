class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = 0
        r = len(nums) - 1
        write = len(nums) - 1
        res = [0] * len(nums)
        while l <= r:
            if abs(nums[l]) > abs(nums[r]):
                res[write] = nums[l] ** 2
                l += 1
            else:
                res[write] = nums[r] ** 2
                r -= 1
            write -= 1
        return res



        