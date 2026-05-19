class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums) 
        l, r, = 0, n-1
        pos = n - 1
        result = [0] * n
        while l <= r:
            left_square = nums[l] ** 2
            right_square = nums[r] ** 2

            if left_square > right_square:
                result[pos] = left_square
                l += 1
            else:
                result[pos] = right_square
                r -= 1
            pos -= 1
        return result

                


            
        