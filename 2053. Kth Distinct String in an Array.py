"""
A distinct string is a string that is present only once in an array.

Given an array of strings arr, and an integer k, return the kth distinct string present in arr. If there are fewer than k distinct strings, return an empty string "".

Note that the strings are considered in the order in which they appear in the array.
"""
class Solution(object):
    def kthDistinct(self, arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """
        cache = {}
        for word in arr:
            if word in cache:
                cache[word] += 1
            else:
                cache[word] = 1

        for word in arr:
            if cache[word] == 1:
                k -= 1
            if k == 0:
                return word

        return ""