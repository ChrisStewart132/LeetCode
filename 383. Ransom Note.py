'''
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.
'''
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        cache = {}
        for char in magazine:
            cache[char] = cache[char] + 1 if char in cache else 1

        for char in ransomNote:
            if char not in cache or cache[char] < 1:
                return False
            cache[char] -= 1

        return True