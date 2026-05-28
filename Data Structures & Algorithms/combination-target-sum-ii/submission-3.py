class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # sort the array to handle duplicate conditions
        candidates.sort()
        res = []

        def dfs(i, curr, total):
            # base condition
            if total == target:
                res.append(curr.copy())
                return
            if i >= len(candidates) or total > target:
                return

            # case to include num in curr
            curr.append(candidates[i])
            dfs(i+1, curr, total + candidates[i])
            curr.pop()

            #EXCLUDE (skip duplicates)
            
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i+1, curr, total)

        dfs(0, [], 0)
        return res
