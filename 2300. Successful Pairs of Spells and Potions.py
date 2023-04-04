class Solution(object):
    def search(self, arr, target, spell):
        l, r = 0, len(arr)
        while l < r:
            m = (l + r) // 2
            if arr[m]*spell < target:
                l = m + 1 
            else:
                r = m      
        return r

    def successfulPairs(self, spells, potions, success):
        """
        :type spells: List[int]
        :type potions: List[int]
        :type success: int
        :rtype: List[int]
        """
        p = sorted(potions)
        output = []

        for spell in spells:
            i = self.search(p, success, spell)

            if i < len(p) and p[i]*spell < success:
                while i < len(p):
                    i += 1
                    if p[i] >= target:
                        break

            if i < len(p):
                output.append(len(p) - i)
            else:
                output.append(0)
        return output
