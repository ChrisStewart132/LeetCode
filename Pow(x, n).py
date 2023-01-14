'''
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
'''
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        elif n < 0:
            return self.myPow(1/x, -n)
        elif n % 2 == 0:
            return (self.myPow(x, n//2))**2
        else:
            return self.myPow(x, n-1) * x