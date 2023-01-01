'''
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.
'''
class Solution(object):
    def reverseString(self, s, i=0):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        if i == len(s):
            return
        
        self.reverseString(s, i+1)
        
        if i >= len(s) // 2:
            temp = s[len(s)-1-i]
            s[len(s)-1-i] = s[i]
            s[i] = temp

        