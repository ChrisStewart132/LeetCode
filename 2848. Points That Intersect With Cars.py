'''
You are given a 0-indexed 2D integer array nums representing the coordinates of the cars parking on a number line. For any index i, nums[i] = [starti, endi] where starti is the starting point of the ith car and endi is the ending point of the ith car.

Return the number of integer points on the line that are covered with any part of a car.
'''
class Solution(object):
    def numberOfPoints(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: int
        """
        first = min([min(p) for p in nums])
        last = max([max(p) for p in nums])
        #print(first, last)
        cache = [0 for i in range(first, last+1)]
        for start, end in nums:
            for i in range(start-first, end+1-first):
                cache[i] = 1
        return sum(cache)