'''
In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

    The town judge trusts nobody.
    Everybody (except for the town judge) trusts the town judge.
    There is exactly one person that satisfies properties 1 and 2.

You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi.

Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.
'''
class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        n_trusts_others = [0 for x in range(n)]
        n_trusted_by_others = [0 for x in range(n)]
        for edge in trust:
            src, dst = edge[0]-1, edge[1]-1
            n_trusts_others[src] = 1
            n_trusted_by_others[dst] += 1

        for i in range(n):
            if n_trusts_others[i] == 0 and n_trusted_by_others[i] == n-1:
                return i+1

        return -1