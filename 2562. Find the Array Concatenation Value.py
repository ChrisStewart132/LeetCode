'''
You are given a 0-indexed integer array nums.

The concatenation of two numbers is the number formed by concatenating their numerals.

    For example, the concatenation of 15, 49 is 1549.

The concatenation value of nums is initially equal to 0. Perform this operation until nums becomes empty:

    If there exists more than one number in nums, pick the first element and last element in nums respectively and add the value of their concatenation to the concatenation value of nums, then delete the first and last element from nums.
    If one element exists, add its value to the concatenation value of nums, then delete it.

Return the concatenation value of the nums.
'''
class Solution(object):
    def n_decimal_digits(self, num):
        return len(str(num))

    def findTheArrayConcVal(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) >= 2:
            rd = self.n_decimal_digits(nums[-1])
            l = nums[0] * (10**(rd))
            r = nums[-1]
            #print(l,r,l+r)
            return l+r + self.findTheArrayConcVal(nums[1:-1])
        elif len(nums) == 1:
            return nums[0]
        else:
            return 0
        