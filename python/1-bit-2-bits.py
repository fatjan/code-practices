class Solution:
    def isOneBitCharacter(self, bits):
		# begin at the start
        i = 0
		# traverse the list
        while i < len(bits):
			#  we need two bits to represent this char, skip to +2th index 
            if bits[i] == 1:
                i += 2
				# last decoded char 2bits long
                flag = False
           
		    # we only need one bit to represent
            else:
                i+=1
				# last decoded char 1 bit long
                flag = True
        return flag

answer = Solution()
print(answer.isOneBitCharacter([1, 0, 0]))
print(answer.isOneBitCharacter([1, 1, 1, 0, 0]))


# We have two special characters. The first character can be represented by one bit 0. The second character can be represented by two bits(10 or 11).

# Now given a string represented by several bits. Return whether the last character must be a one-bit character or not. The given string will always end with a zero.

# Example 1:
# Input:
# bits = [1, 0, 0]
# Output: True
# Explanation:
# The only way to decode it is two-bit character and one-bit character. So the last character is one-bit character.
# Example 2:
# Input:
# bits = [1, 1, 1, 0]
# Output: False
# Explanation:
# The only way to decode it is two-bit character and two-bit character. So the last character is NOT one-bit character.
# Note:

# 1 <= len(bits) <= 1000.
# bits[i] is always 0 or 1.
