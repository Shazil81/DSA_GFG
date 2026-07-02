class myQueue:

    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def enqueue(self, x):
        # Implement the enqueue operation
        self.in_stack.append(x)
        
        
    def dequeue(self):
        # Implement the dequeue operation
        if self.front() == -1:
            return -1
        # front() call karne ke baad out_stack ready hoga, bas pop kar do
        return self.out_stack.pop()


    def front(self):
        # Return the front element of the queue
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        
        if not self.out_stack:
            return -1        
        
        return self.out_stack[-1]


    def size(self):
        # Return the current size of the queue
        return len(self.in_stack) + len(self.out_stack)