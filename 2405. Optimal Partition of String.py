class Solution(object):
    def partitionString(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = 0
        chars = set()
        for char in s:
            if char not in chars:
                chars.add(char)
            else:
                n += 1
                chars = set(char)
        return n+1