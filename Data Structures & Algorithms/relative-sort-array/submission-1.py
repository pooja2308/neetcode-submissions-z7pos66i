class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res = []
        from collections import Counter
        freq_count = Counter(arr1)

        for i in range(len(arr2)):
            if arr2[i] in freq_count:
                res.extend([arr2[i]] * freq_count.get(arr2[i]))
                del freq_count[arr2[i]]

        for num in sorted(freq_count):
            res.extend([num] * freq_count.get(num))
        return res



        