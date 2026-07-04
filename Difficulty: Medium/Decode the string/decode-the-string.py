class Solution:
    def decodedString(self, s):
        count_stack = []
        string_stack = []
        curr_string = ""
        number = 0

        for ch in s:
            if ch.isdigit():
                number = number*10 + int(ch)
            elif ch == "[":
                count_stack.append(number)
                string_stack.append(curr_string)

                number = 0
                curr_string = ""
            elif ch == "]":
                number_count = count_stack.pop()
                prev_string = string_stack.pop()

                curr_string = prev_string + (number_count * curr_string)
            
            else:
                curr_string += ch
        
        return curr_string
        