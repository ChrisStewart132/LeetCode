'''
A permutation perm of n + 1 integers of all the integers in the range [0, n] can be represented as a string s of length n where:

    s[i] == 'I' if perm[i] < perm[i + 1], and
    s[i] == 'D' if perm[i] > perm[i + 1].

Given a string s, reconstruct the permutation perm and return it. If there are multiple valid permutations perm, return any of them.
'''
class Solution(object):
    def diStringMatch(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        output = []
        a,b = 0, len(s)
        for symbol in s:
            if symbol == 'I':
                output.append(a)
                a += 1
            else:
                output.append(b)
                b -= 1
        if s[-1] == 'I':
            output.append(a)
        else:
            output.append(b)
        return output