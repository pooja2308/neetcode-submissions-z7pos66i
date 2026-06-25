class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        

        def canShip(capacity: int) -> bool:
            weight_so_far = 0
            used_day = 1
            for weight in weights:
                if weight + weight_so_far > capacity:
                    used_day += 1
                    weight_so_far = 0
                weight_so_far += weight
            return used_day <= days



        
        
        while l < r:
            mid = (l + r) // 2
            if canShip(mid):
                r = mid
            else:
                l = mid + 1

        return l



        