class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        res = 0
        single_nums = []
        for num in nums:
            res ^= num
        
        diff = res & -res
        first_grp = 0
        second_grp = 0
        for num in nums:
            if diff & num:
                first_grp ^= num
            else:
                second_grp ^= num
        return [first_grp, second_grp]
        