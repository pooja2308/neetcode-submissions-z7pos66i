class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        res = False
        count = 0
        for word in words:
            res = all(ch in allowed for ch in word)
            if res:
                count += 1
        return count
        