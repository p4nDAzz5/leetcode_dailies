class MinStack(object):

    def __init__(self):
        self.stack = []
        self.minElem = 0

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        print(self.stack, self.minElem)
        if len(self.stack) == 0:
            self.minElem = val
            self.stack.append(val)
        elif self.minElem < val:
            self.stack.append(2*val-self.minElem)
            self.minElem = val
        else:
            self.stack.append(val)

    def pop(self):
        """
        :rtype: None
        """
        if len(self.stack) >= 1:
            if self.stack[-1] < self.minElem:
                self.minElem = 2*self.minElem-self.stack[-1]
            del self.stack[-1]

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.minElem

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()