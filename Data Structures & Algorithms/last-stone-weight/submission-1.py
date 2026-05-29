import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        n = len(stones)
        for i in range(n):
            stones[i] = -stones[i]
        heapq.heapify(stones) # heapify does in space so O(1)
        

        while len(stones) > 1:
            largest = heapq.heappop(stones)
            second_largest = heapq.heappop(stones)

            if largest != second_largest:
                heapq.heappush(stones, (largest - second_largest))
            
        if len(stones) == 1:
            return -heapq.heappop(stones) 
        else:
            return 0
    
# Time complexity- O(n log n), n times 
# because of while loop and we are going to push or pop in half of the tree 

