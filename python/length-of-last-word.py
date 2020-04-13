class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        string = s.split(' ')
        new_str = []
        for item in string:
            if item != '':
                new_str.append(item)
        print(new_str)
        return len(new_str[len(new_str) - 1])

a = Solution()
print(a.lengthOfLastWord('a '))
print(a.lengthOfLastWord("b   a    "))
