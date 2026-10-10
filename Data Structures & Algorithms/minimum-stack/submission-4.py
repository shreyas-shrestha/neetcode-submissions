class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        self.minStack.append(float('inf'))
    
    def push(self, val: int):
        self.stack.append(val)
        if val <= self.minStack[len(self.minStack)-1]:
            self.minStack.append(val)
    
    def pop(self):
        current = self.stack.pop()
        if current == self.minStack[len(self.minStack)-1]:
            self.minStack.pop()
    
    def top(self) -> int:
        return self.stack[len(self.stack)-1]
    
    def getMin(self) -> int:
        return self.minStack[len(self.minStack)-1]