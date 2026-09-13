class Solution:
	def mergeOverlap(self, arr):
		n = len(arr)
        arr.sort()
        curr_start = arr[0][0]
        curr_end = arr[0][1]
        res = []
        for i in range(1,n):
            if arr[i][0] <= curr_end:
                curr_end = max(arr[i][1], curr_end)
            else:
                res.append([curr_start, curr_end])
                curr_start = arr[i][0]
                curr_end = arr[i][1]
        res.append([curr_start, curr_end])
        return res
		