class Solution:
    def arrangeCoins(self, n: int) -> int:
        l, r  = 1, n
        while l <= r:
            mid = (l + r) // 2
            coins_needed = mid * (mid + 1) // 2 # we need to find the largest k such that: 
            # k × (k + 1) / 2 ≤ n
            if coins_needed > n:
                r = mid - 1
            elif coins_needed < n:
                l = mid + 1
            else:
                return mid
        return r
            