# Implement a trie with insert, search, and startsWith methods.

# Example:

# Trie trie = new Trie()

# trie.insert("apple")
# trie.search("apple")
# // returns true
# trie.search("app")
# // returns false
# trie.startsWith("app")
# // returns true
# trie.insert("app")
# trie.search("app")
# // returns true
# Note:

# You may assume that all inputs are consist of lowercase letters a-z.
# All inputs are guaranteed to be non-empty strings.


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s = ''

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        self.s += word
        return self.s

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        return word in self.s

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cond = False
        pref_len = len(prefix)
        split_s = self.s.split(' ')
        for i in range(len(split_s)):
            if split_s[i][:pref_len] == prefix:
                cond = True
                break
        return cond


# Your Trie object will be instantiated and called as such:
word = 'apple'
prefix = 'app'
obj = Trie()
print(obj)
obj.insert(word)
print(obj)
param_2 = obj.search(word)
print(param_2)
param_3 = obj.startsWith(prefix)
print(param_3)
