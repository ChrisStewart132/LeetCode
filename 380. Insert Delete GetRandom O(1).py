'''
Implement the RandomizedSet class:

    RandomizedSet() Initializes the RandomizedSet object.
    bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
    bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
    int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.

You must implement the functions of the class such that each function works in average O(1) time complexity.
'''
from random import randint
class RandomizedSet(object):

    def __init__(self):
        self.cache = {}

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.cache:
            return False
        self.cache[val] = True
        return True
        

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.cache:
            del self.cache[val]
            return True
        return False

    def getRandom(self):
        """
        :rtype: int
        """
        i = randint(0, len(self.cache.keys())-1)
        return self.cache.keys()[i]

        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()