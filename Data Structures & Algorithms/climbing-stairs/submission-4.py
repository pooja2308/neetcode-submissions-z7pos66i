class Solution:
    def climbStairs(self, n: int) -> int:
        # solution 1: this will fail on some of the test cases as it is so slow
        # Time complexity: O(2^n) as we are calling the same function, Space: O(n) 
        # if n == 1:
        #     return 1
        # if n == 2:
        #     return 2
        # return self.climbStairs(n-2) + self.climbStairs(n-1)

        # solution 2
        cache = {1:1, 2:2}
        def f(n):
            if n in cache:
                return cache[n]
            else:
                cache[n] = f(n-2) + f(n-1)
                return cache[n] 
        return f(n)
                
        
        
        
        