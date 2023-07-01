'''
You are given a positive integer num consisting only of digits 6 and 9.

Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).
'''
class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        stack = []
        while num > 0:
            digit = num % 10
            num -= digit
            num /= 10
            stack.append(digit)

        for i in range(len(stack)-1,-1,-1):
            if stack[i] == 6:
                stack[i] = 9
                break

        return sum([stack[i] * 10**i for i in range(len(stack)-1,-1,-1)])
        

