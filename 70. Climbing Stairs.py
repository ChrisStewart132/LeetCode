'''
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
'''
class Solution(object):
    cache = {}
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        elif n < 0:
            return 0
        else:
            left = self.cache[n-1] if n-1 in self.cache else self.climbStairs(n-1)
            self.cache[n-1] = left
            right = self.cache[n-2] if n-2 in self.cache else self.climbStairs(n-2)
            self.cache[n-2] = right
            return  left + right