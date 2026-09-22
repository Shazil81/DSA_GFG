class Solution:
    def activitySelection(self, start: list[int], end: list[int]) -> int:
        # Greedy algo
        meetings = []
        n = len(start)
        # ek list banaya jisme start or end daala
        for i in range(n):
            meetings.append((start[i], end[i]))
        # fir end k basis pe sort kiya
        meetings.sort(key = lambda x: x[1])

        curr_end = meetings[0][1]
        count = 1 # pehla meeting count hoga hamesha isi liye

        for i in range(1, n):
            # curr_end ka agar start se chhota hai tb hi to overlap nhi krega
            # or naya meeting ho payega
            if curr_end < meetings[i][0]:
                count+=1
                # curr_end ko update kr do taaki next start se compare ho ske
                curr_end = meetings[i][1]
        return count