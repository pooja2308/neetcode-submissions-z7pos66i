class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        result = max(piles)
        l, r = 1, max(piles)
        

        while l <= r:
            hour_est = 0
            mid = (l + r) // 2
            for pile in piles:
                hour_est += math.ceil(pile / mid)
            if hour_est <= h:
                result = min(result, mid)
                r = mid - 1
            else:
                l = mid + 1
        return result


        