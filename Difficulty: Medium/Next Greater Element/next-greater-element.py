class Solution:
    def nextLargerElement(self, arr):
        # Monotonic stack pe based hai
        n = len(arr)
        ans = [-1] * n
        stack = []
        for i in range(n-1, -1, -1):
            # naya agar element aata h to check hoga ki stack ka top se bada hai to pop hoga
            while len(stack) != 0 and stack[-1] <= arr[i]:
                stack.pop()
            # or jab stack khali nhi h to ans me update hoga
            if len(stack) != 0:
                ans[i] = stack[-1]
            # Last me add kr do us element ko bs
            stack.append(arr[i])
        return ans
        