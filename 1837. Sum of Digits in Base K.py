'''
Given an integer n (in base 10) and a base k, return the sum of the digits of n after converting n from base 10 to base k.

After converting, each digit should be interpreted as a base 10 number, and the sum should be returned in base 10.
'''
class Solution(object):
    def convert_to_base(self, n, k):
        stack = []
        while n > 0:
            stack.append(n%k)
            n //= k
        return stack
        #return sum([(10**i)*stack[i] for i in range(len(stack)-1, -1, -1)])
    def sumBase(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        stack = self.convert_to_base(n, k)
        return sum(stack)
