'''
You are given an array of n pairs pairs where pairs[i] = [lefti, righti] and lefti < righti.

A pair p2 = [c, d] follows a pair p1 = [a, b] if b < c. A chain of pairs can be formed in this fashion.

Return the length longest chain which can be formed.

You do not need to use up all the given intervals. You can select pairs in any order.
'''
class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        sorted_pairs = sorted(pairs, key=lambda x:x[1])
        output, prev = 1, sorted_pairs[0]
        for pair in sorted_pairs:
            if prev[1] < pair[0]:
                output += 1
                prev = pair
        return output