'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

'''
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        d = {')':'(', ']':'[', '}':'{'}
        for char in s:
            if char in "([{":
                stack += [char]
            else:
                try:
                    if stack.pop() != d[str(char)]:
                        return False
                except IndexError:
                    return False
        return len(stack) == 0
