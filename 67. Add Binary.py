'''
Given two binary strings a and b, return their sum as a binary string.
'''
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        '''c = 0
        l, r = min(len(a), len(b)), max(len(a), len(b))
        n1 = a if len(a) == l else b
        n2 = b if len(a) == l else a
        
        for i in range(l):
            c = c + 2**(l-i-1) if n1[i] == '1' else 0
            c = c + 2**(r-i-1) if n2[i] == '1' else 0
        for i in range(l, r):
            c = c + 2**(r-i-1) if n2[i] == '1' else 0

        return bin(c)[2:]'''
        return bin(int("0b"+a, 2) + int("0b"+b, 2))[2:]