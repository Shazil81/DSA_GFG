class Solution:
	def pushZerosToEnd(self, arr):
    	# two pointers approach
    	n = len(arr)
    	left = 0
    	right = 0
    	
    	while right < n:
    	    # jaise hi right pointer non zero pe phonchega tb swap or left += 1
    	    if arr[right] != 0:
    	        arr[right], arr[left] = arr[left], arr[right]
    	        left += 1
    	    right += 1
    	