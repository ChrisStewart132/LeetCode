'''
You are given an array of strings names, and an array heights that consists of distinct positive integers. Both arrays are of length n.

For each index i, names[i] and heights[i] denote the name and height of the ith person.

Return names sorted in descending order by the people's heights.
'''
class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        arr = [(names[i], heights[i]) for i in range(len(names))]
        sorted_arr = sorted(arr, key=lambda x:x[1], reverse=True)
        return [x[0] for x in sorted_arr]