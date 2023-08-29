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
        elif n < 0:# could improve efficiency here
            return self.myPow(1/x, -n)
        elif n % 2 == 0:
            res = (self.myPow(x, n//2))
            return res**2
        else:
            return self.myPow(x, n-1) * x