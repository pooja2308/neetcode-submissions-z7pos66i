class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closetoOpen = {')':'(',
        '}':'{',
        ']':'['}
        for st in s:
            print(stack)
            print(st)
            if stack and stack[-1] == closetoOpen.get(st):
                stack.pop()
            else:
                stack.append(st)

        return True if not stack else False






        


            
                
        