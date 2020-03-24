class Solution:

    def printName(self, name):
        print(name)
    
    def okPrintName(self, other_name):
        print(other_name)
        self.printName('janna')

coba = Solution()

coba.okPrintName('fatma')