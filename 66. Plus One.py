'''
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.
'''
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i = len(digits)-1
        digits[i] += 1
        while digits[i] == 10 and i > 0:
            digits[i] = 0
            i -= 1
            digits[i] += 1
        
        if digits[0] == 10:
            digits[0] = 0
            return [1] + digits

        return digits