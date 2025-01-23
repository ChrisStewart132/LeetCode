'''
Given a string s of lower and upper case English letters.

A good string is a string which doesn't have two adjacent characters s[i] and s[i + 1] where:

    0 <= i <= s.length - 2
    s[i] is a lower-case letter and s[i + 1] is the same letter but in upper-case or vice-versa.

To make the string good, you can choose two adjacent characters that make the string bad and remove them. You can keep doing this until the string becomes good.

Return the string after making it good. The answer is guaranteed to be unique under the given constraints.

Notice that an empty string is also good.
'''
class Solution(object):
    def bad(self, a, b):
        return a.lower() == b.lower() and ((a.islower() and b.isupper()) or (a.isupper() and b.islower()))
    def _makeGood(self, s, i=1):
        """
        :type s: str
        :rtype: str
        """
        if i >= len(s):
            return s
        a,b = s[i-1], s[i]
        if self.bad(a,b):
            s = s[:i-1] + s[i+1:]
        return self._makeGood(s, i+1)
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """
        current = self._makeGood(s)
        while True:# keep processing the string until it stops changing
            next = self._makeGood(current)
            if len(current) == len(next):
                break
            else:
                current = next
        return current
        