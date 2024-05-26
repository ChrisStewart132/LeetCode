'''
Given a 0-indexed string word and a character ch, reverse the segment of word that starts at index 0 and 
ends at the index of the first occurrence of ch (inclusive). If the character ch does not exist in word, do nothing.

    For example, if word = "abcdefd" and ch = "d", then you should reverse the segment that starts at 0 and 
    ends at 3 (inclusive). The resulting string will be "dcbaefd".

Return the resulting string.
'''
class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        i = word.find(ch)
        if i:
            return word[:i+1][::-1] + word[i+1:]
        return word
        