'''
Given an integer x, return true if x is a
palindrome
, and false otherwise.
'''
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        stack = []# obtain all digits
        while x > 0:
            r = x%10
            stack.append(r)
            x -= r
            x /= 10

        for i in range(0, len(stack)//2):# confirm the stack is symmetrical
            if stack[i] != stack[-i-1]:
                return False

        return True