'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
'''
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        cache = {}
        for i in range(len(s)):
            cache[s[i]] = cache[s[i]] + 1 if s[i] in cache else 1
            cache[t[i]] = cache[t[i]] - 1 if t[i] in cache else -1

        return all([n == 0 for n in cache.values()])