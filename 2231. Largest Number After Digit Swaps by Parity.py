'''
You are given a positive integer num. You may swap any two digits of num that have the same parity (i.e. both odd digits or both even digits).

Return the largest possible value of num after any number of swaps.
'''
class Solution(object):
    def largestInteger(self, num):
        """
        :type num: int
        :rtype: int
        """
        digits, even_digits, odd_digits = [], [], []
        while num > 0:
            digit = num%10
            if digit%2 == 0:
                even_digits.append(digit)
            else:
                odd_digits.append(digit)
            digits.append(digit)
            num //= 10

        even_digits = sorted(even_digits)
        odd_digits = sorted(odd_digits)

        output = 0
        for i in range(len(digits)):
            output *= 10
            digit = digits.pop()
            if digit % 2 == 0:
                output += even_digits.pop()
            else:
                output += odd_digits.pop()
        return output
        