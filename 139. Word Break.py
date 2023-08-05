'''
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.
'''
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        words = set(wordDict)
        l = max([len(x) for x in wordDict])
        cache = {}

        def _wordBreak(word):
            if word in cache:
                return cache[word]

            if len(word) == 0:
                return True

            solutions = []
            for i in range(1, min(l, len(word))+1):
                if word[:i] in words:
                    cache[word[i:]] = _wordBreak(word[i:])
                    solutions.append(cache[word[i:]])

            return any(solutions)


        return _wordBreak(s)