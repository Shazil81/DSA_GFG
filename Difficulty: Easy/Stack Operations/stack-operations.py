class myStack:
    # Define your stack
    def __init__(self):
        self.stack = []

    def push(self, x):
        # insert x into stack
        self.stack.append(x)
        

    def pop(self):
        # remove top ele from stack
        if not self.stack:
            return
        self.stack.pop()

    def peek(self):
        # return top of stack
        if not self.stack:
            return
        return self.stack[-1]

    def getSize(self):
        # return current size of stack
        return len(self.stack)

    def isEmpty(self):
        # check whether stack is empty
        return len(self.stack) == 0
