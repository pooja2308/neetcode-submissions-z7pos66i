class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        anagram_items = defaultdict(list)
        for st in strs:
            count=[0] * 26
            for c in st:
                count[ord(c) - ord("a")] += 1
            anagram_items[tuple(count)].append(st)
        return list(anagram_items.values())



