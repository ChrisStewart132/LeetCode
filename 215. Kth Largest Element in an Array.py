'''
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?
'''
import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap = []# min heap

        for i in range(k):# add k elements to the heap
            heappush(heap, nums[i])

        for i in range(k, len(nums)):# check remaining numbers
            if heap[0] < nums[i]:# if num is < heaps min, pop the min and add the larger number
                item = heapreplace(heap, nums[i])# pop smallest and add next

        return heap[0]# the heap min is the kth largest element