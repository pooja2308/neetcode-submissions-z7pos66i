class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque
        output = []
        l = r = 0
        q = deque() #index

        
        while r < len(nums):
            # pop smaller value from the queue
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # remove left value from window if greater 
            if l > q[0]: # or q[0] < (r - k + 1) by checking first value of deque and current index r and k value
                q.popleft()
            
            # check if right pointer is greater than or equal to k vlaue
            if r + 1 >= k:
                output.append(nums[q[0]])
                l += 1
            
            r += 1
        return output
        

        