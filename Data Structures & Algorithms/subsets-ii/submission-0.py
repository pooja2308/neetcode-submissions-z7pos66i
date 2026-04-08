class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        subsets = []

        def backtracking(i):
            # base case
            if i >= len(nums):
                res.append(subsets.copy())
                return
            
            # include scenarios
            subsets.append(nums[i])
            backtracking(i + 1)
            subsets.pop()

            # avoid duplicates
            while i+1 < len(nums) and nums[i+1] == nums[i]:
                i += 1
                
            backtracking(i + 1)
        backtracking(0)
        return res




        