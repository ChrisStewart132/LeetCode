'''
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
'''
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        phrase = [x for x in s.lower() if x.isalnum()]
        n = len(phrase)
        for i in range(n//2):
            if phrase[i] != phrase[n-i-1]:
                return False
        return True