'''
You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once).

Return the sum of lengths of all good strings in words.
'''
class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        output = 0
        for word in words:
            cache = {}
            for char in word:
                try:
                    cache[char] += 1
                except KeyError:
                    cache[char] = 1
                    
            valid = True
            for char, n in cache.items():
                if chars.count(char) < n:
                    valid = False
                    break

            if valid:
                output += len(word)

        return output

