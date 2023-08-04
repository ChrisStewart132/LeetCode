'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
'''
class Solution(object):
    map = ['','','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
    def letterCombinations(self, digits, i=0, candidate=""):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(candidate) == len(digits):
            return [candidate] if len(digits) > 0 else []


        output = []
        for symbol in self.map[int(digits[i])]:
            child = self.letterCombinations(digits, i+1, candidate + symbol)
            output += child

        return output
        