class Solution:
    def largestRectangleArea(self, heights):
        stack = []
        max_area = 0
        n = len(heights)

        for i in range(n+1): # n+1 sentinel kyun ki last saare elements ko stack me se hta dena h isi liye
            if i < n:
                curr_height = heights[i]
            else:
                curr_height = 0 # wohi sentinel k liye
            
            while stack and heights[stack[-1]] > curr_height: # jab ko bar aisa mile jo stack k top baar se chhota ho tab pop krte jayenge jab tk wo stack k top se bada n ho jaye
                top_idx = stack.pop()
                height = heights[top_idx]

                if stack:
                    width = i - stack[-1] - 1  # width mera wohi hoga jo stack ka top hoga pop krne k baad wha se i tk jab stack khali n ho tb
                else:
                    width = i
                
                max_area = max(max_area, height*width)
            
            stack.append(i) # stack me indices store kr rhe hain
        
        return max_area
        
    def maxArea(self, matrix):
        max_area = 0
        n_cols = len(matrix[0])
        heights = [0] * n_cols  # ek height array maintain krenge jo mera histogram k trh treat hoga

        for row in matrix:
        # Step 1: heights array update karo is row ke hisaab se
            for col in range(n_cols):
                if row[col] == 1:
                    heights[col] += 1     # 1 mila -> height badhao
                else:
                    heights[col] = 0
            # Step 2: is row tak ka "histogram" ready hai, ispar LC-84 wala function chalao
            max_area = max(max_area, self.largestRectangleArea(heights))
        
        return max_area
        