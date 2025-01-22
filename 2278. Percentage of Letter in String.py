'''
Given a string s and a character letter, return the percentage of characters in s that equal letter rounded down to the nearest whole percent.
'''
class Solution(object):
    def percentageLetter(self, s, letter):
        """
        :type s: str
        :type letter: str
        :rtype: int
        """
        return int((s.count(letter) / float(len(s))) * 100)
        