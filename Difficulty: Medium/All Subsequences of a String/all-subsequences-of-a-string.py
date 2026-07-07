class Solution:
    def solve(self, index,subset, s, res):
        if index >= len(s):  # base case
            res.append("".join(subset.copy()))  # kyun ki copy nhi krenge to null aa jayega delete bhi to kr rhe h
            return
        subset.append(s[index])
        self.solve(index+1, subset, s, res)  # pick wale ko call diya
        subset.pop()  # jo pick kiya wapas jatae waqt pop kr diya
        self.solve(index+1, subset, s, res)  # ab bina pick wale ko call diya
	def powerSet(self, s):
		# yha pe recursion se krte hain
        subset = []
        s = list(s)
        res = []
        self.solve(0, subset, s, res)
        res.sort()
        return res
		