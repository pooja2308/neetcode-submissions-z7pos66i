class MyQueue:

    def __init__(self):
        self.stackk = []
        

    def push(self, x: int) -> None:
        self.stackk.append(x)

    def pop(self) -> int:
        pop_ele = self.stackk.pop(0)
        return pop_ele
        

    def peek(self) -> int:
        front_ele =  self.stackk[0]
        return front_ele
        

    def empty(self) -> bool:
        if len(self.stackk) == 0:
            return True
        return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()