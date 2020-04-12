class Solution:
    def entityParser(self, text):
        mark = ['&quot;', '&apos;', '&amp;', '&gt;', '&lt;', '&frasl;']
        entity = ["\"", "\'", '&', '>', '<', '/']
        new_text = text
        for i in range(len(mark)):
            new_text = new_text.replace(mark[i], entity[i])
        return new_text

a = Solution()
print(a.entityParser("&amp; is an HTML entity but &ambassador; is not."))
