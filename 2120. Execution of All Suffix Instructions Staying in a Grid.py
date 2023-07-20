'''
There is an n x n grid, with the top-left cell at (0, 0) and the bottom-right cell at (n - 1, n - 1). You are given the integer n and an integer array startPos where startPos = [startrow, startcol] indicates that a robot is initially at cell (startrow, startcol).

You are also given a 0-indexed string s of length m where s[i] is the ith instruction for the robot: 'L' (move left), 'R' (move right), 'U' (move up), and 'D' (move down).

The robot can begin executing from any ith instruction in s. It executes the instructions one by one towards the end of s but it stops if either of these conditions is met:

    The next instruction will move the robot off the grid.
    There are no more instructions left to execute.

Return an array answer of length m where answer[i] is the number of instructions the robot can execute if the robot begins executing from the ith instruction in s.
'''
class Solution(object):
    def executeInstructions(self, n, startPos, s):
        """
        :type n: int
        :type startPos: List[int]
        :type s: str
        :rtype: List[int]
        """
        output = []
        for i in range(len(s)):# for each sub command
            output.append(0)# this sub commands possible executions
            y, x = startPos
            for j in range(i, len(s)):# for each part of the sub command  
                # move
                if s[j] == "L":
                    x -= 1
                elif s[j] == "R":
                    x += 1
                elif s[j] == "U":
                    y -= 1
                else:
                    y += 1

                # continue if bot inside grid else sub-command potential completed
                if x >= 0 and x < n and y >= 0 and y < n:
                    output[i] += 1
                else:
                    break

        return output