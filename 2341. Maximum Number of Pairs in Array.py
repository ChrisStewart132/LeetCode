'''
You are given a 0-indexed integer array nums. In one operation, you may do the following:

    Choose two integers in nums that are equal.
    Remove both integers from nums, forming a pair.

The operation is done on nums as many times as possible.

Return a 0-indexed integer array answer of size 2 where answer[0] is the number of pairs that are formed and answer[1] is the number of leftover integers in nums after doing the operation as many times as possible.
'''
class Solution(object):
    def numberOfPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        cache = {}
        for num in nums:
            cache[num] = cache[num] + 1 if num in cache else 1

        return sum([v//2 for v in cache.values()]), sum([1 for k in cache.keys() if cache[k] % 2 == 1])

        '''output = [0, 0]# pairs, leftovers
        for num in cache.keys():
            if cache[num] % 2 == 1:
                output[1] += 1
                cache[num] -= 1 
            output[0] += cache[num]
        output[0] /= 2
        return output'''