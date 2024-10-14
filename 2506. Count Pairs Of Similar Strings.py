'''
You are given a 0-indexed string array words.

Two strings are similar if they consist of the same characters.

    For example, "abca" and "cba" are similar since both consist of characters 'a', 'b', and 'c'.
    However, "abacba" and "bcfd" are not similar since they do not consist of the same characters.

Return the number of pairs (i, j) such that 0 <= i < j <= word.length - 1 and the two strings words[i] and words[j] are similar.
'''
class Solution(object):
    def similarPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        output = 0
        word_sets = [set(word) for word in words]
        for i, s1 in enumerate(word_sets):
            for j in range(i+1, len(word_sets)):
                output = output+1 if s1==word_sets[j] else output
        return output
            
