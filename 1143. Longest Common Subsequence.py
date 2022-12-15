'''
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

    For example, "ace" is a subsequence of "abcde".

A common subsequence of two strings is a subsequence that is common to both strings.
'''
class Solution(object):
    def longestCommonSubsequence(self, text1, text2, i=0, j=0, cache=None):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        # init
        if cache == None:
            cache = {}
            i = len(text1)-1
            j = len(text2)-1

        # base case
        if i == -1 or j == -1:
            return 0

        if text1[i] == text2[j]:
            mid = cache[(i-1,j-1)] if (i-1,j-1) in cache else self.longestCommonSubsequence(text1, text2, i-1, j-1, cache)
            cache[(i-1,j-1)] = mid
            return 1 + mid
        else:
            left = cache[(i-1,j)] if (i-1,j) in cache else self.longestCommonSubsequence(text1, text2, i-1, j, cache)
            cache[(i-1,j)] = left
            right = cache[(i,j-1)] if (i,j-1) in cache else self.longestCommonSubsequence(text1, text2, i, j-1, cache)
            cache[(i,j-1)] = right
            return max(left, right)
