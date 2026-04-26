class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
    
        # get the count of each int, i.i. {1: 1, 2: 2, 3: 3}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        # append the int in the freq list for each count, i.e. [[], [1], [2], [3], [], [], []]. Bucket sort and put 
        # the count in respective bucket.
        for key, v in count.items():
            freq[v].append(key)
        
        # get the top k values by iterating through the freq 
        # list from the end and compare the value len result with k
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for j in freq[i]:
                res.append(j)
                if len(res) == k:
                    return res
        return []

         


        

        




        