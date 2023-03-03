class Solution(object):
    def _check(self, i, haystack, needle):
        if haystack[i] == needle[0]:
            if i+len(needle)-1 < len(haystack) and haystack[i+len(needle)-1] == needle[-1]:
                if haystack[i:i+len(needle)] == needle: 
                    return True
        return False

    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        i = 0
        while i < len(haystack):
            if self._check(i, haystack, needle):
                return i
            else:
                i += 1
        return -1

