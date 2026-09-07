class Solution:
    def solve(self, index, arr, subset, char_map, res):
        if index >= len(arr): # base condition
            res.append("".join(subset)) # kyun ki string chahiye isi liye list ko string bnaya
            return

        digit_str = str(arr[index])

        # If the digit has mapped characters (e.g., 2-9)
        if digit_str in char_map and char_map[digit_str]:
            for ch in char_map[digit_str]:
                subset.append(ch)
                self.solve(index + 1, arr, subset, char_map, res)
                subset.pop()
        else:
            # If digit is 0 or 1 (no letter mapping), skip it and proceed to next digit
            self.solve(index + 1, arr, subset, char_map, res)
            
            
    def possibleWords(self, arr: list[int]) -> list[str]:
        
        char_map = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"} # ye char_map is liye bnaya h ki access kr sken 
        res = []
        self.solve(0, arr, [], char_map, res)
        return res
        
