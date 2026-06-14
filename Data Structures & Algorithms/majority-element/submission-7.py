class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority_ele_threshold = len(nums) // 2
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

            if count[num] > majority_ele_threshold:
                return num
        

        


        