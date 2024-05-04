'''
You are given two 0-indexed integer arrays nums1 and nums2 of sizes n and m, respectively.

Consider calculating the following values:

    The number of indices i such that 0 <= i < n and nums1[i] occurs at least once in nums2.
    The number of indices i such that 0 <= i < m and nums2[i] occurs at least once in nums1.

Return an integer array answer of size 2 containing the two values in the above order.
'''
class Solution(object):
    def findIntersectionValues(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        s1, s2 = set(nums1), set(nums2)
        return [sum([1 for num in nums1 if num in s2]), sum([1 for num in nums2 if num in s1])]