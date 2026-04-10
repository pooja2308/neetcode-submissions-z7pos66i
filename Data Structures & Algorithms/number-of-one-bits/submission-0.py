class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0

        # count the number of 1s after each bitwise AND
        while n !=0:
            n = n & (n-1)
            ans += 1
        return ans

        # Time complexity O(NumOnes) 
        # Space complexity O(1)
        