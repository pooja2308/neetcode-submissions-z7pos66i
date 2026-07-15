class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for _ in range(len(nums) + 1)]
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        for key, v in count.items():
            freq[v].append(key)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for j in freq[i]:
                res.append(j)
                if len(res) == k:
                    return res
        return []

            
            