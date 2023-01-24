'''
Given an array of integers nums, sort the array in ascending order and return it.

You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.
'''
class Solution(object):
    def merge(self, left, right, l=0, r=0):
        result = []
        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                result.append(left[l])
                l+=1
            else:
                result.append(right[r])
                r+=1
                
        # append the remaining sorted list
        if l < len(left):
            result += left[l:]
        else:
            result += right[r:]

        return result
    
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == 1:
            return nums        
        left = self.sortArray(nums[:len(nums)//2])
        right = self.sortArray(nums[len(nums)//2:])
        return self.merge(left, right)
        