'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 
'''
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        stack = [strs[0]]

        while len(stack) > 0:
            s = stack.pop()
            if len(s) > 1:
                #stack.append(s[1:])
                stack.append(s[:-1])
            if all([s in x[:len(s)] for x in strs]):
                return s

        return ""

                
                
