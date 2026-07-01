class Solution:
    def median(self, mat):
    	# n -> rows, m-> cols
    	n = len(mat)
    	m = len(mat[0])
    	res = []
    	
    	for row in mat:
    	    for num in row:
    	        res.append(num)
    	
    	res.sort()
    	
    	N = len(res)
    	
    	if N % 2 != 0:
    	    return res[N//2]
    	else:
    	    return (res[N//2 - 1] + res[N//2])/2
    	        
    	