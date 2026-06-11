class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack= []
        

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
        
        
        

    def pop(self) -> None:
        if self.is_empty():
            raise IndexError("Stack is Empty")

        last_ele = self.stack.pop()
        if last_ele==self.min_stack[-1]:
            self.min_stack.pop()
        
        

    def top(self) -> int:
        if self.is_empty():
            raise IndexError("Stack is Empty")

        return self.stack[-1]
        
    def is_empty(self):
        return len(self.stack) == 0

    def getMin(self) -> int:
        return self.min_stack[-1]
        
