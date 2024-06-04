'''
There is a malfunctioning keyboard where some letter keys do not work. All other keys on the keyboard work properly.

Given a string text of words separated by a single space (no leading or trailing spaces) and a string brokenLetters
 of all distinct letter keys that are broken, return the number of words in text you can fully type using this keyboard.
'''
class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        """
        :type text: str
        :type brokenLetters: str
        :rtype: int
        """
        return sum([all([letter not in set(word) for letter in brokenLetters]) for word in text.split()])