class Solution:
    def calculateSpan(self, arr):
        # Monotonic decreasing stack
        ans = []
        stack = []
        for i in range(len(arr)):
            span = 1
            while stack and stack[-1][0] <= arr[i]:
                previous_price, prev_span = stack.pop()
                span += prev_span
            
            ans.append(span)
            
            stack.append((arr[i], span))
        
        return ans
    
            
        