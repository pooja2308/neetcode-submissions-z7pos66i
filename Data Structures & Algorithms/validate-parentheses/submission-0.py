class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {')': '(',
        '}': '{',
        ']': '['}
        for st in s:
            if st in closeToOpen:
                if stack and stack[-1] == closeToOpen[st]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(st)
        return True if not stack else False 




        


            
                
        