'''
You are given two 2D integer arrays, items1 and items2, representing two sets of items. Each array items has the following properties:

    items[i] = [valuei, weighti] where valuei represents the value and weighti represents the weight of the ith item.
    The value of each item in items is unique.

Return a 2D integer array ret where ret[i] = [valuei, weighti], with weighti being the sum of weights of all items with value valuei.

Note: ret should be returned in ascending order by value.
'''
class Solution(object):
    def mergeSimilarItems(self, items1, items2):
        """
        :type items1: List[List[int]]
        :type items2: List[List[int]]
        :rtype: List[List[int]]
        """
        cache = {}
        for value, weight in items1:
            try:
                cache[value] += weight
            except KeyError:
                cache[value] = weight
        for value, weight in items2:
            try:
                cache[value] += weight
            except KeyError:
                cache[value] = weight
        return sorted([[value, weight] for value, weight in cache.items()], key=lambda x: x[0])