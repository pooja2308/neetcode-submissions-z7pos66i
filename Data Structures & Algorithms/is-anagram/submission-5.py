class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # space complexity is O(n +m) 
        # from collections import Counter
        # if Counter(s) == Counter(t):
        #     return True
        # return False  

        # space complexity is O(n +m) 
        # s_count = {}   
        # t_count = {}   

        # for i, c in enumerate(s):
        #     s_count[c] = 1 + s_count.get(c, 0)
        
        # for i, c in enumerate(t):
        #     t_count[c] = 1 + t_count.get(c, 0)

        # if s_count == t_count:
        #     return True
        # return False

        # space complexity is O(1) 
        if len(s) != len(t):
            return False
        count = [0] * 26
        for c in s:
            count[ord(c) - ord("a")] += 1

        for c in t:
            count[ord(c) - ord("a")] -= 1
            if count[ord(c) - ord("a")] < 0:
                return False
        
        return True




        

            
            

