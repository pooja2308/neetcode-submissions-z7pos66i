class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        result = []
        if not nums:
            return []
        for num in nums:
            if num == 1:
                result.insert(len(nums), num)
            elif num % 2 == 0:
                result.insert(0, num)
            else:
                result.insert(len(nums), num)
        return result