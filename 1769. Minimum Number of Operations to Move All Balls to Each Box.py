'''
You have n boxes. You are given a binary string boxes of length n, where boxes[i] is '0' if the ith box is empty, and '1' if it contains one ball.

In one operation, you can move one ball from a box to an adjacent box. Box i is adjacent to box j if abs(i - j) == 1. Note that after doing so, there may be more than one ball in some boxes.

Return an array answer of size n, where answer[i] is the minimum number of operations needed to move all the balls to the ith box.

Each answer[i] is calculated considering the initial state of the boxes.
'''
class Solution(object):
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """
        loutput = [0 for x in boxes]
        l = [int(x) for x in boxes]
        for i in range(1, len(boxes)):
            l[i] += l[i-1]
            loutput[i] += l[i-1] + loutput[i-1]

        routput = [0 for x in boxes]
        r = [int(x) for x in boxes]
        for i in range(len(boxes)-2,-1,-1):
            r[i] += r[i+1]
            routput[i] += r[i+1] + routput[i+1]

        return [loutput[i] + routput[i] for i in range(len(boxes))]
