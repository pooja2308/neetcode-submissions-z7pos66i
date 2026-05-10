class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindorme(l, r):
            while l < r:
                if s[l].lower() != s[r].lower():
                    return False 
                l += 1
                r -= 1
            return True

        left, right = 0, len(s) - 1
        while left < right:
            if s[left].lower() != s[right].lower():
                return is_palindorme(left + 1, right) or is_palindorme(left, right - 1)
            left += 1
            right -= 1
        return True


                

