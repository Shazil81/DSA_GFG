from collections import deque


class myStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque() 

    def push(self, x):
        # push element on top
        self.q2.append(x)
        # Move all from main to helper
        while self.q1:
            self.q2.append(self.q1.popleft())
        # swap helper becomes main
        self.q1, self.q2 = self.q2, self.q1
        
    def pop(self):
        # remove top element
        if not self.q1:
            return  
        return self.q1.popleft()
        
    def top(self):
        # return top element
        if not self.q1:
            return -1
        return self.q1[0]
        
    def size(self):
        # return current size
        return len(self.q1) + len(self.q2)
        
