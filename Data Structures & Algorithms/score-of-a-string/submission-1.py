class Solution:
    def scoreOfString(self, s: str) -> int:
        summ = 0
        for i in range(0, len(s)-1):
            summ += abs(ord(s[i + 1]) - ord(s[i]))
        return summ

        