class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count_mag = {}

        for i in range(len(magazine)):
            count_mag[magazine[i]] = 1 + count_mag.get(magazine[i], 0)

        for note in ransomNote:
            if count_mag.get(note, 0) == 0:
                return False

            count_mag[note] -= 1 
        return True

    
        # for i in range(len(ransomNote)):
        #     count_note[ransomNote[i]] = 1 + count_note.get(ransomNote[i], 0)

        # res = all(k in count_mag.keys() and v <= count_mag[k] for k, v in count_note.items())
        # if res:
        #     return True
        # return False
        