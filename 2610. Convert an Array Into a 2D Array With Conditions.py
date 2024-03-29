'''
You are given an integer array nums. You need to create a 2D array from nums satisfying the following conditions:

    The 2D array should contain only the elements of the array nums.
    Each row in the 2D array contains distinct integers.
    The number of rows in the 2D array should be minimal.

Return the resulting array. If there are multiple answers, return any of them.

Note that the 2D array can have a different number of elements on each row.
'''
class Solution(object):
    def findMatrix(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        output = [[]]
        cache = [set()]
        for n in nums:
            done = False
            for i in range(len(output)):
                if n not in cache[i]:
                    output[i].append(n)
                    cache[i].add(n)
                    done = True
                    break

            if not done:
                output.append([n])
                cache.append(set([n]))

        return output