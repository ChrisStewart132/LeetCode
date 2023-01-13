'''
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.

Given n, calculate F(n)
'''
class Solution(object):
    cache = {}
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return n
        else:
            x = self.cache[n-1] if n-1 in self.cache else self.fib(n-1)
            self.cache[n-1] = x
            y = self.cache[n-2] if n-2 in self.cache else self.fib(n-2)
            self.cache[n-2] = y
            return x + y