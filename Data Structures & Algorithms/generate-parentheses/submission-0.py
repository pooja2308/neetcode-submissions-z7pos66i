class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        well_formed = []
        def backtracking(num_open, num_close):
            # base case
            if n == num_open == num_close:
                res.append("".join(well_formed))
                return 

            if num_open < n:
                well_formed.append("(")
                backtracking(num_open + 1, num_close)
                well_formed.pop()
            
            if num_close < num_open:
                well_formed.append(")")
                backtracking(num_open, num_close + 1)
                well_formed.pop()

        backtracking(0, 0)
        return res



        