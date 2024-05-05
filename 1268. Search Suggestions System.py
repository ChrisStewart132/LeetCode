'''
You are given an array of strings products and a string searchWord.

Design a system that suggests at most three product names from products after each character of searchWord is typed. Suggested products should have common prefix with searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.

Return a list of lists of the suggested products after each character of searchWord is typed.
'''
class Solution(object):
    def searchLeft(self, arr, target, l=0, r=None):
        if r == None:
            r = len(arr)-1
        length = len(target)
        while l+1 < r:
            m = (l+r)//2
            val = arr[m][:length]
            if val < target:
                l = m+1
            else:
                r = m
        if arr[l][:length] == target:
            return l
        elif l+1 < len(arr) and arr[l+1][:length] == target:
            return l+1
        return -1
    
    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        products.sort()
        output = []
        for i in range(len(searchWord)):
            target = searchWord[:i+1]
            left_index = self.searchLeft(products, target)
            suggestions = [products[l] for l in range(left_index, min(left_index+3, len(products))) if products[l][:i+1] == target]
            #print(target, suggestions)
            output.append(suggestions)

        return output