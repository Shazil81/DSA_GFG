class Solution:
    def kokoEat(self, arr, k):
        # Optimal Solution Binary Search (Search Space ka khela hai to binary search lgega kyun ki soretd order me search space le rhe h)
        low = 1
        high = max(arr)
        res = high

        while low <= high:
            mid = (low+high)//2
            total_hours = 0
            for pile in arr:
                total_hours += math.ceil(pile/mid)
            
            if total_hours <= k: # condition k hisab se agar utna me hua to usse bhi minimum me check kre lenge 
                res = mid
                high = mid - 1
            else: # agar mera total hours zyada ho jayega to speed ko badha denge jo ki mera mid hai as a speed
                low = mid + 1
        
        return res
        