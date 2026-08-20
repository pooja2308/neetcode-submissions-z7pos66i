class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = 0
        j = 0
        while i < len(word) and j < len(abbr):
            if abbr[j].isalpha():
                if abbr[j] != word[i]:
                    return False
                i += 1
                j += 1
            else:
                if abbr[j] == '0':
                    return False

                skip = 0
                while j < len(abbr) and abbr[j].isdigit():
                    skip = skip * 10 + int(abbr[j])
                    j += 1
                i += skip
        return i == len(word) and j == len(abbr)

            




        
        