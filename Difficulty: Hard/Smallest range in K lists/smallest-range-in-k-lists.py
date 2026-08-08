import heapq
class Solution:
    def findSmallestRange(self, mat):
        # heap + sliding window : optimal one
        heap = []
        curr_max = float('-inf')

        # har list ka pehla element push krte hain
        for i in range(len(mat)):
            heapq.heappush(heap, (mat[i][0], i, 0))
            curr_max = max(curr_max, mat[i][0])
        
        best_range = [float('-inf'), float('inf')]
        
        while heap:
            curr_min, list_idx, ele_idx = heapq.heappop(heap)

            # range update
            if curr_max - curr_min < best_range[1] - best_range[0]:
                best_range = [curr_min, curr_max]

            # agar len k equal ho gya ele_idx yaani jo list me or elements nhi bache
            if ele_idx + 1 == len(mat[list_idx]):
                break
            
            # next element push
            val = mat[list_idx][ele_idx + 1]
            heapq.heappush(heap, (val, list_idx, ele_idx + 1))
            curr_max = max(curr_max, val)
        
        return best_range
        