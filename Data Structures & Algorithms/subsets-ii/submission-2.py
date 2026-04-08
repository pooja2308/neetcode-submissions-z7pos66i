class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def backtracking(start, path):
            # base case
            # if i >= len(nums):
            #     res.append(path[:])
            #     return
            
            # # include scenarios(Binary decision at each index)
            # subsets.append(nums[i])
            # backtracking(i + 1)
            # subsets.pop()

            # # avoid duplicates
            # while i+1 < len(nums) and nums[i+1] == nums[i]:
            #     i += 1
                
            # backtracking(i + 1)


            # optimal approach
            res.append(path[:])
            for i in range(start, len(nums)):
                if i > start and nums[i-1] == nums[i]:
                    continue
                path.append(nums[i])
                backtracking(i+1, path)
                path.pop()
        backtracking(0, [])
        return res




        