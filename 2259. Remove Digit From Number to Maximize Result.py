'''
You are given a string number representing a positive integer and a character digit.

Return the resulting string after removing exactly one occurrence of digit from number
 such that the value of the resulting string in decimal form is maximized. The test cases
  are generated such that digit occurs at least once in number.
'''
class Solution(object):
    def removeDigit(self, number, digit):
        """
        :type number: str
        :type digit: str
        :rtype: str
        """
        max_num = "0"
        for i in range(len(number)):
            if number[i] == digit:
                new_number = number[:i] + number[i+1:]
                max_num = max(max_num, new_number)
        return max_num