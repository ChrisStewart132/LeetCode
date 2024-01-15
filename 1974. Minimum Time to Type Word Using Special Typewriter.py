'''
There is a special typewriter with lowercase English letters 'a' to 'z' arranged in a circle with a pointer. A character can only be typed if the pointer is pointing to that character. The pointer is initially pointing to the character 'a'.
'''
class Solution(object):
    def minTimeToType(self, word):
        """
        :type word: str
        :rtype: int
        """
        # a=97, z=122
        output = 0
        pos = 'a'
        for c in word:
            d = abs(ord(c)-ord(pos))
            #print("dist:",d,"pos:",pos,"char:",c)
            output += min(d, (26-abs(d)))+1
            pos = c
        return output