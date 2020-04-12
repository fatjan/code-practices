class Solution:
    def reverseBits(self, n):
        # '{:032b}'.format(n)
        n_bin = '{:32b}'.format(n)
        n_bin = n_bin.replace(' ', '0')
        print(n_bin)
        n_bin_reverse = n_bin[-1::-1]
        return int(n_bin_reverse, 2)


my_int = 43261596
a = Solution()
print(a.reverseBits(43261596))
print(a.reverseBits(4294967293))
