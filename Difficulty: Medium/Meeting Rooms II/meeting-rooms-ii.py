class Solution:
    def minMeetingRooms(self, start, end):
        start.sort()
        end.sort()
        
        n = len(start)
        i = j = 0
        rooms = 0
        max_rooms = 0
        
        while i < n:
            if start[i] < end[j]: # yaani room nhi hai
                rooms += 1
                i += 1
                max_rooms = max(max_rooms, rooms)
            else: # room khali hua
                rooms -= 1
                j += 1
        
        return max_rooms
        
        
