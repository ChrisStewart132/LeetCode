'''
Given an array of strings words, return the first palindromic string in the array. If there is no such string, return an empty string "".

A string is palindromic if it reads the same forward and backward.
'''
class Solution(object):
    def firstPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        def isPalindrome(w):
          return all(w[i] == w[-i-1] for i in range(len(w)//2))
        for word in words:
          if isPalindrome(word):
            return word
        return ""