class Solution:
	def singleNum(self, arr):
		# Step 1: get all xor first
          total_xor = 0
          for num in arr:
              total_xor ^= num

          # Step 2: find righmost set bit
          rm_set_bit = total_xor & (-total_xor)

          # Step 3: divide in two groups and xor each group
          x = 0
          y = 0
          for num in arr:
              if num & rm_set_bit:
                  x ^= num
              else:
                  y ^= num

          ans = [x, y]
          ans.sort()
          return ans
