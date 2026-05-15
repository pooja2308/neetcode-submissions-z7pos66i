class MyStack:

    def __init__(self):
        self.queue = []
        
    def push(self, x: int) -> None:
        self.queue.append(x)
        

    def pop(self) -> int:
        pop_element = self.queue.pop(-1)
        return pop_element
        

    def top(self) -> int:
        front_element = self.queue[-1]
        return front_element

    def empty(self) -> bool:
        return True if len(self.queue) == 0 else False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()