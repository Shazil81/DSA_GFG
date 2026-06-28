class Solution:
    def leastWeightCapacity(self, arr, D):
        # Optimal solution Binary Search
        low = max(arr) # max weight hi to hoga uska low wala capacity nhi to kuchh ko utha payega or kuchh ko nhi
        high = sum(arr)  # max capacity
        ans = high

        while low <= high:
            mid = (low+high)//2
            total_days = 1 # day 1 se initialize nhi to last me ek miss hoga
            curr_sum = 0
            for weight in arr:
                if curr_sum + weight > mid: # jab mid se bada ho jaye yaani ki 1 din ka max capacity
                    total_days += 1
                    curr_sum = weight
                else:
                    curr_sum += weight
            
            if total_days <= D:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return ans
        