'''
Given a string s, return true if s is a good string, or false otherwise.

A string s is good if all the characters that appear in s have the same number of occurrences (i.e., the same frequency).
'''
class Solution(object):
    def areOccurrencesEqual(self, s):
        """
        :type s: str
        :rtype: bool
        """
        cache = {}
        for char in s:
            cache[char] = cache[char] + 1 if char in cache else 1
        return max(cache.values()) == min(cache.values())