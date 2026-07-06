class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq_count = {}
        res = []
        for n in nums:
            freq_count[n] = 1 + freq_count.get(n, 0)
        for k, v in sorted(freq_count.items(), key=lambda x: (x[1], -x[0])):
            res.extend([k]*v)
        return res

        