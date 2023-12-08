'''
Given an integer n, return any array containing n unique integers such that they add up to 0.
'''
class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        output = [] if n % 2 == 0 else [0]
        for i in range(1, n//2+1):
          output += [i,-i]
        return output