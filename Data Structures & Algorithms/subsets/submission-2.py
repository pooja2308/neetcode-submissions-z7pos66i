class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        def dfs(i):
            # base case
            if i >= len(nums):
                res.append(subset.copy())
                return 

            # decision to include nums[i]
            subset.append(nums[i])
            print(f'include{subset}')
            dfs(i + 1)
            
            # decision NOT to include nums[i]
            subset.pop()
            print(f'exclude{subset}')
            dfs(i + 1)
        dfs(0)
        return res

        # bit manipulation, mask is like a switchboard where each bit 
        # represents 1 -> include in subset , 0 -> exclude
        # res = []
        # n = len(nums)
        # for mask in range(1 << n): # 2**n
        #     subset = []
        #     for i in range(n):
        #         if mask & (1 << i):
        #             subset.append(nums[i])
        #     res.append(subset)
        # return res


        