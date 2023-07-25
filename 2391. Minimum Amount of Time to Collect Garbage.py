'''
You are given a 0-indexed array of strings garbage where garbage[i] represents the assortment of garbage at the ith house. garbage[i] consists only of the characters 'M', 'P' and 'G' representing one unit of metal, paper and glass garbage respectively. Picking up one unit of any type of garbage takes 1 minute.

You are also given a 0-indexed integer array travel where travel[i] is the number of minutes needed to go from house i to house i + 1.

There are three garbage trucks in the city, each responsible for picking up one type of garbage. Each garbage truck starts at house 0 and must visit each house in order; however, they do not need to visit every house.

Only one garbage truck may be used at any given moment. While one truck is driving or picking up garbage, the other two trucks cannot do anything.

Return the minimum number of minutes needed to pick up all the garbage.
'''
class Solution(object):
    def garbageCollection(self, garbage, travel):
        """
        :type garbage: List[str]
        :type travel: List[int]
        :rtype: int
        """
        m,p,g = None, None, None# last house to visit for each type
        for i in range(len(garbage)-1,-1,-1):
            if m == None and "M" in garbage[i]:
                m = i
            if p == None and "P" in garbage[i]:
                p = i
            if g == None and "G" in garbage[i]:
                g = i
            if m and p and g:
                break

        t = garbage[0].count("M") + garbage[0].count("P") + garbage[0].count("G")

        if m:
            for i in range(1, m+1):
                t += garbage[i].count("M")
                t += travel[i-1]

        if p:
            for i in range(1, p+1):
                t += garbage[i].count("P")
                t += travel[i-1]

        if g:
            for i in range(1, g+1):
                t += garbage[i].count("G")
                t += travel[i-1]

        return t