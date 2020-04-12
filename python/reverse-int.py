class Solution:
    def reverse(self, x):
        x_string = str(x)
        if str(x)[0] == '-':
            x_string = x_string[-1:0:-1]
            return '-' + x_string
        x_string = x_string[-1::-1]
        if str(x)[-1] == '0':
            return x_string[1:]
        else:
            return x_string

a = Solution()
print(a.reverse(123))
print(a.reverse(-123))
print(a.reverse(120))



# Given a 32-bit signed integer, reverse digits of an integer.

# Example 1:

# Input: 123
# Output: 321
# Example 2:

# Input: -123
# Output: -321
# Example 3:

# Input: 120
# Output: 21
# Note:
# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
