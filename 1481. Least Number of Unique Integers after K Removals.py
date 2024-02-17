'''
Given an array of integers arr and an integer k. Find the least number of unique integers after removing exactly k elements.
'''
class Solution(object):
    def findLeastNumOfUniqueInts(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        cache = {}
        for n in arr:
            if n in cache:
                cache[n] += 1
            else:
                cache[n] = 1
        
        pairs = sorted(cache.items(), key=lambda x:x[1], reverse=True)
        while k > 0:
            if k <= pairs[-1][1]:
                pairs[-1] = (pairs[-1][0], pairs[-1][1]-k)
                if pairs[-1][1] == 0:
                    pairs.pop()
                break
            k -= pairs[-1][1]
            pairs.pop()
        
        return len(pairs)
        