class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        subs = []
        for i, word in enumerate(words):
            for j, other in enumerate(words):
                if i != j and word in other:
                    subs.append(word)
                    break
        return subs


        