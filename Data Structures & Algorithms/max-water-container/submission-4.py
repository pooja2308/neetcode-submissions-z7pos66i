class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maximun = 0
        while l < r:
            length = (r - l)
            height = min(heights[r], heights[l])
            current_maximum = length * height
            maximun= max(maximun, current_maximum)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return maximun


        