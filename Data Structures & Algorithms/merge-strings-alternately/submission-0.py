class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l , r = 0, 0
        output = []
        while l < len(word1) and r < len(word2):
            output.append(word1[l].lower())
            output.append(word2[r].lower())
            l += 1
            r += 1
        if len(word1) > len(word2):
            output.append(word1[len(word2):].lower())
        else:
            output.append(word2.lower()[len(word1):])
        return "".join(output)

        