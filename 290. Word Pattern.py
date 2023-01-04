'''
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.
'''
class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        d = {}
        assigned_words = set()
        words = s.split(" ")
        if len(words) != len(pattern):
            return False
            
        for i in range(len(words)):
            if pattern[i] not in d:
                if words[i] in assigned_words:
                    return False
                d[pattern[i]] = words[i]
                assigned_words.add(words[i])
            elif d[pattern[i]] != words[i]:
                return False
        return True
                