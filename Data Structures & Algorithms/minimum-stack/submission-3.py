class MinStack:

    def __init__(self):
        self.MinStack = []
        self.SubStack = []
        self.smallest = float("inf")
        
    def push(self, val: int) -> None:
        self.smallest = min(self.smallest,val)

        self.SubStack.append(self.smallest)
        
        self.MinStack.append(val)
        
    def pop(self) -> None:
        if len(self.MinStack) != 0:
            self.MinStack.pop()

            self.SubStack.pop()

            if len(self.SubStack) == 0:
                self.smallest = float("inf")
            else:
                self.smallest = self.SubStack[-1]


    def top(self) -> int:
        if len(self.MinStack) != 0:
            return self.MinStack[-1]
        
    def getMin(self) -> int:
        if len(self.MinStack) != 0:
            return self.SubStack[-1]

