'''
Hercy wants to save money for his first car. He puts money in the Leetcode bank every day.

He starts by putting in $1 on Monday, the first day. Every day from Tuesday to Sunday, he will put in $1 more than the day before. On every subsequent Monday, he will put in $1 more than the previous Monday.

Given n, return the total amount of money he will have in the Leetcode bank at the end of the nth day.
'''
class Solution(object):
    def totalMoney(self, n, depth=0):
        """
        :type n: int
        :rtype: int
        """
        cache = [1]
        for i in range(1, n):
            cache.append(cache[-7]+1) if i % 7 == 0 else cache.append(cache[-1] + 1)
        return sum(cache)
