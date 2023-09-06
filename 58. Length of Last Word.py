'''
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal
substring
consisting of non-space characters only.
'''

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.rstrip().split(" ")[-1])

        l = 0
        for i in range(len(s)-1,-1,-1):
            if s[i] == " " and l == 0:
                continue
            elif s[i] == " ":
                break
            else:
                l += 1
        return l


