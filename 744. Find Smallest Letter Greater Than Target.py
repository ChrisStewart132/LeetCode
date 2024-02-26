'''
You are given an array of characters letters that is sorted in non-decreasing order, and a character target. There are at least two different characters in letters.

Return the smallest character in letters that is lexicographically greater than target. If such a character does not exist, return the first character in letters.
'''
class Solution(object):
    def searchRight(self, arr, target):
        """
        find the index where elements are > target
        """
        l, r = 0, len(arr)-1
        while l+1 < r:# until 2 elements in search space
            m = (l+r)//2
            if arr[m] > target:
                r = m# cut off right of m
            else:
                l = m# cut off left of m
        #[,n,n,n,...,arr[l], arr[r],....,n,n,n]
        if arr[l] > target:
            return l
        elif arr[r] > target:
            return r
        return -1# no values exist > target

    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        i = self.searchRight(letters, target)
        return letters[i] if i != -1 else letters[0]
        