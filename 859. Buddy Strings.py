class Solution(object):
    def buddyStrings(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        if len(s) == len(goal):
            i,j = 0, len(s)-1
            while i < j:
                if s[i] != goal[i]:
                    break
                i += 1

            while j > i:
                if s[j] != goal[j]:
                    break
                j -= 1

            if i == j:# no swaps needed
                if s[i] != goal[i]:
                    return False
                return len(s) != len(set(s))# if set(s) == s then no swaps possible

            if s[j] != goal[i] or s[i] != goal[j]:
                return False
                
            for i in range(i+1, j):
                if s[i] != goal[i]:
                    return False
            return True
            #return s[i+1:j] == goal[i+1:j]

        return False