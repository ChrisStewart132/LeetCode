'''
You are given a string s consisting of lowercase English letters, and you are allowed to perform operations on it. In one operation, you can replace a character in s with another lowercase English letter.

Your task is to make s a palindrome with the minimum number of operations possible. If there are multiple palindromes that can be made using the minimum number of operations, make the lexicographically smallest one.

A string a is lexicographically smaller than a string b (of the same length) if in the first position where a and b differ, string a has a letter that appears earlier in the alphabet than the corresponding letter in b.

Return the resulting palindrome string.
'''
class Solution(object):
    def makeSmallestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        output = ""
        for i in range(len(s)//2):
            l,r = s[i], s[len(s)-1-i]
            if l == r:
                output += l
            elif ord(l) < ord(r):
                output += l
            else:
                output += r

        start = len(output)-1
        if len(s) % 2 == 1:
            output += s[len(s)//2]

        for i in range(start,-1,-1):
            output += output[i]

        return output