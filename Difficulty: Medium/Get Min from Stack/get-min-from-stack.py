class SpecialStack:

    def __init__(self):
        # Define Stack
        self.items = []
        
    
    def push(self, val):
        # Add an element to the top of Stack
        if len(self.items) == 0:
            self.items.append([val, val]) # ele = zeroth pos, min = 1st pos   double element is liye ki ek min hoga or ek val baar baar update jayega
        else:
            # yha pe min val update ho ja rha h
            mini = min(self.items[-1][1], val)
            self.items.append([val, mini])

    
    def pop(self):
        # Remove the top element from the Stack
        if not self.items:
            return
        self.items.pop()

    
    def peek(self):
        # Returns top element of Stack
        if not self.items:
            return -1
        return self.items[-1][0]
        
    def isEmpty(self):
        # Check if the stack is empty
        return len(self.items) == 0

    
    def getMin(self):
        # Finds minimum element of Stack
        if not self.items:
            return -1
        return self.items[-1][1]