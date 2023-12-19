'''
You are given a 0-indexed array words consisting of distinct strings.

The string words[i] can be paired with the string words[j] if:

    The string words[i] is equal to the reversed string of words[j].
    0 <= i < j < words.length.

Return the maximum number of pairs that can be formed from the array words.

Note that each string can belong in at most one pair.
'''
class Solution(object):
    def maximumNumberOfStringPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        n = 0
        for i in range(len(words)):# for each word
            for j in range(i+1, len(words)):# compare words ahead
                  valid = True
                  for k in range(len(words[i])//2+1):
                      if words[i][k] != words[j][-k-1]:
                          valid = False
                          break
                  n = n + 1 if valid else n
        return n