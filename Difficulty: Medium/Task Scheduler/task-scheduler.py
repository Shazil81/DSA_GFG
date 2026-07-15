class Solution:
    def leastInterval(self, N, K, tasks):
        # Greedy + Math: Optimal One
        # Step 1: frequency count karo
        freq = {}
        for t in tasks:
            freq[t] = freq.get(t, 0) + 1

        # step 2: max_freq jo max hai wo nikalo or uska count nikalo
        max_freq = 0
        max_freq_count = 0
        for count in freq.values():
            if count > max_freq:
                max_freq = count
                max_freq_count = 1
            elif count == max_freq:
                max_freq_count += 1
        # Step 3: Formula lgao 
        ans = (max_freq - 1) * (K + 1) + max_freq_count

        return max(ans, N)
        