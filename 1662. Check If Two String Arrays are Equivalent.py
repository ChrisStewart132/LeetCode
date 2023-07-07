'''
Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.

A string is represented by an array if the array elements concatenated in order forms the string.
'''
class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        i,j = 0,0
        for word in word1:
            for char in word:
                try:
                    if char != word2[i][j]:
                        return False
                except IndexError:
                    return False
                j+=1
                if j >= len(word2[i]):
                    i,j = i+1, 0

        return True if i == len(word2) else False

