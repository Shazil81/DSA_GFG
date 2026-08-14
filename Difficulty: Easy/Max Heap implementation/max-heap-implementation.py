class maxHeap:

    def __init__(self):
        # Initialize your data members
        self.heap = []
        
    def heapify_up(self, ind):
        parent_ind = (ind - 1)//2
        if ind > 0 and self.heap[parent_ind] < self.heap[ind]:
            self.heap[parent_ind], self.heap[ind] = self.heap[ind], self.heap[parent_ind]
            self.heapify_up(parent_ind)
    
    def heapify_down(self, ind):
        largest_ind = ind
        left_child = 2*ind + 1
        right_child = 2*ind + 2
        if left_child < len(self.heap) and self.heap[left_child] > self.heap[largest_ind]:
            largest_ind = left_child
        if right_child < len(self.heap) and self.heap[right_child] > self.heap[largest_ind]:
            largest_ind = right_child
        if largest_ind != ind:
            self.heap[largest_ind], self.heap[ind] = self.heap[ind], self.heap[largest_ind]
            self.heapify_down(largest_ind)
    # Insert x into the heap
    def push(self, x: int):
        self.heap.append(x)
        self.heapify_up(len(self.heap)-1)


    # Remove the top (maximum) element
    def pop(self):
        # code here
        if not self.heap:
            return
        
        if len(self.heap) == 1:
            self.heap.pop()
            return
        
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)

    # Return the top element or -1 if empty
    def peek(self) -> int:
        if not self.heap:
            return -1
        return self.heap[0]


    # Return the number of elements in the heap
    def size(self) -> int:
        # code here
        return len(self.heap)