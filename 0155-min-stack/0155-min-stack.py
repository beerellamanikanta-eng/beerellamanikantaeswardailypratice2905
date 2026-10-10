
class MinStack(object):

    def __init__(self):
        self.stack = []
        self.minstack = []
    def push(self, value):
        self.stack.append(value)
        if not self.minstack or value <= self.minstack[-1]:
            self.minstack.append(value)
    def pop(self):
        if self.stack[-1] == self.minstack[-1]:
            self.minstack.pop()
        self.stack.pop()
    def top(self):
        return self.stack[-1]
    def getMin(self):
        return self.minstack[-1]
