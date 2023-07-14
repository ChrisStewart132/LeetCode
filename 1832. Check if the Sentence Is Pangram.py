'''
A pangram is a sentence where every letter of the English alphabet appears at least once.

Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.
'''
class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        s = set([chr(i) for i in range(97, 97+26)])
        for char in sentence:
            if char in s:
                s.remove(char)
            if len(s) == 0:
                return True
        return True if len(s) == 0 else False