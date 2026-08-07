import heapq
class Solution:
    def getMedian(self, arr):
        max_heap = []  # lower half (negated, taaki max-heap simulate ho)
        min_heap = []  # upper half (normal min-heap)
        result = []    # har step ka median store karega

        for num in arr:
            # Step 1: naya number pehle max_heap me daalo (negate karke)
            heapq.heappush(max_heap, -num)

            # Step 2: Cross-check — max_heap ka max, min_heap ke min se bada nahi hona chahiye
            if max_heap and min_heap and (-max_heap[0] > min_heap[0]):
                val = -heapq.heappop(max_heap)
                heapq.heappush(min_heap, val)

            # Step 3: max_heap, min_heap se 1 se zyada bada na ho
            if len(max_heap) > len(min_heap) + 1:
                val = -heapq.heappop(max_heap)
                heapq.heappush(min_heap, val)

            # Step 4: min_heap kabhi bhi max_heap se bada na ho
            if len(min_heap) > len(max_heap):
                val = heapq.heappop(min_heap)
                heapq.heappush(max_heap, -val)

            # ab is step ka median nikalo
            if len(max_heap) > len(min_heap):
                median = float(-max_heap[0])
            else:
                median = (-max_heap[0] + min_heap[0]) / 2.0

            result.append(median)

        return result
        