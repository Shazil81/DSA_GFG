class Solution:
    def majorityElement(self, arr):
        # Moore's voting algorithm
        n = len(arr)
        el = 0
        count = 0
        for num in arr:
            # sab se pehle ek element lenge or uska count = 1 krenge
            if count == 0:
                el = num
                count+=1
            # agar wohi element wapas aaya to count increment krenge
            elif el == num:
                count+=1
            # agar nhi aaya to count decrement krenge
            else:
                count-=1
        # ab tk mera count me majority element agar exist krta hoga to aa gya hoga
        count = 0
        # wohi element ko count kr lenge agar n/2 se bada hua count to return
        for num in arr:
            if num == el:
                count+=1
                
        if count > n//2:
                return el
        return -1
        