class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        char_count_from_s = Counter(s)
        char_count_from_t = Counter(t)
        if char_count_from_s != char_count_from_t:
            return False
        return True

        