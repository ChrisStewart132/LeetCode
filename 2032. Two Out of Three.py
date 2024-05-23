'''
Given three integer arrays nums1, nums2, and nums3, return a distinct array containing 
all the values that are present in at least two out of the three arrays. You may return
 the values in any order. 
'''
class Solution(object):
    def twoOutOfThree(self, nums1, nums2, nums3):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :rtype: List[int]
        """
        s1, s2, s3 = set(nums1), set(nums2), set(nums3)
        output = s1.intersection(s2)
        output = output.union(s1.intersection(s3)) 
        output = output.union(s2.intersection(s3))
        return list(output)