class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # this method takes O(n) time complexity    
        seen = {}
        for i, num in enumerate(nums):
            if (target - num) in seen:
                return [seen[(target - num)], i]
            seen[num] = i
        
        # two pointers only works when array is sorted but that would add time complexity here O(n log n)
        # l, r = 0 , len(nums) - 1
        # print(len(nums) - 1)
        # while l < r:
        #     if nums[l] + nums[r] > target:
        #         r -= 1
        #     elif nums[l] + nums[r] < target:
        #         l += 1
            
        #     else:
        #         print(target)
        #         return [l, r]
        # return []
        



        


        