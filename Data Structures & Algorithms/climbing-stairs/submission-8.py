class Solution:
    def climbStairs(self, n: int) -> int:
        # solution 1: this will fail on some of the test cases as it is so slow
        # Time complexity: O(2^n) as we are calling the same function, Space: O(n) 
        # if n == 1:
        #     return 1
        # if n == 2:
        #     return 2
        # return self.climbStairs(n-2) + self.climbStairs(n-1)

        # solution 2(Memoization/cache/top bottom approach)
        # Time comlexity: O(n)
        # Space comlexity: O(n) 
        # cache = {1:1, 2:2}
        # def f(n):
        #     if n in cache:
        #         return cache[n]
        #     else:
        #         cache[n] = f(n-2) + f(n-1)
        #         return cache[n] 
        # return f(n)

        # solution 3(bottom up approach/tabulation)
        # Time comlexity: O(n)
        # Space comlexity: O(n) 
        # if n == 1:
        #     return 1
        # if n == 2:
        #     return 2
        # dp = [0] * n
        # dp[0] = 1
        # dp[1] = 2
        # for i in range(2, n):
        #     dp[i] = dp[i-2] + dp[i-1]
        # return dp[n-1] or dp[-1]

        # bottom up with space complexity = O(1)
        # Time comlexity: O(n)
        if n == 1:
            return 1
        if n == 2:
            return 2
        prev = 1
        cur = 2
        for i in range(2, n):
            prev, cur = cur, (prev + cur)
        return cur





                
        
        
        
        