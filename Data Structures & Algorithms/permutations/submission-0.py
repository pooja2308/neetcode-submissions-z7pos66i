class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        permutation = []
        def backtrack():
            # base case
            if len(permutation) == len(nums):
                res.append(permutation.copy())
                return 

            for num in nums:
                if num not in permutation:
                    permutation.append(num)
                    backtrack()
                    # must undo the step we did in the previous step
                    permutation.pop()

            
        backtrack()
        return res
            

        
        