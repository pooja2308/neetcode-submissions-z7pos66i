class MinStack:

    def __init__(self):
        self.minstack = list()
        

    def push(self, val: int) -> None:
        self.minstack.append(val)
        return None
        

    def pop(self) -> None:
        self.minstack.pop(-1)
        return None
        

    def top(self) -> int:
        return self.minstack [-1]
        

    def getMin(self) -> int:
        return min(self.minstack)
        
