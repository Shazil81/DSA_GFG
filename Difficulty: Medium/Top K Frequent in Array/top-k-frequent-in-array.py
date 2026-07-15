class Solution:
	def topKFreq(self, nums, k):
		# Hashmap + sorting : Not Optimal
        # n = len(arr) - Agar chahiye toh use kar sakte ho
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
            
        # Tu jo bol raha hai uske hisaab se:
        # freq.items() -> (number, frequency)
        # key=lambda x: (x[1], x[0]) -> (frequency, number)
        # reverse=True -> dono descending order me honge
        
        sorted_items = sorted(freq.items(), key=lambda x: (x[1], x[0]), reverse=True)
        
        result = []
        for i in range(k):
            result.append(sorted_items[i][0]) 
                
        # Agar tune reverse=True rakha hai, toh result already sorted hai.
        # Upar wala code seedha return karega.
        return result
		
		