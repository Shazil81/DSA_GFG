class Solution:
    def mergedArray(self,arr, l, mid, r):
        res = []
        left = l
        right = mid+1
        while left<= mid and right<=r:
            if arr[left] <= arr[right]:
                res.append(arr[left])
                left+=1
            else:
                res.append(arr[right])
                right+=1
        while left<=mid:
            res.append(arr[left])
            left+=1
        while right<=r:
            res.append(arr[right])
            right+=1
        for i in range(l, r+1):
            arr[i] = res[i-l]
        return arr
    def mergeSort(self, arr, l, r):
        # code here
        if l >= r:
            return
        mid = (l + r)//2
        self.mergeSort(arr, l, mid)
        self.mergeSort(arr, mid+1, r)
        return self.mergedArray(arr, l, mid, r)
        