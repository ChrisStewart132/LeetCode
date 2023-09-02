'''
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.
'''
class Solution(object):
    cache = [0,1,1]
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        for i in range(len(self.cache), n+1):     
            self.cache.append((i&1) + self.cache[i>>1])
            #self.cache.append((i%2) + self.cache[(i-(i%2))//2])
        return self.cache[:n+1]

        