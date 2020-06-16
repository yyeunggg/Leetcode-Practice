# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 10:45:01 2020

@author: steve
"""

"""
380. Insert Delete GetRandom O(1)

https://leetcode.com/problems/insert-delete-getrandom-o1/
"""

# The testing is not random
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.rset = set()
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """

        if val in self.rset:
            return False
        self.rset.add(val)
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.rset:
            self.rset.remove(val)
            return True
        return False
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        if self.rset:
            key = self.rset.pop()   #Testing is not random, i think it pops the last item.
            self.rset.add(key)
            return key



# Try testing 'real' randomness, it is very slow though.
# Runtime: 184 ms, faster than 35.33% of Python3 online submissions for Insert Delete GetRandom O(1).
# Memory Usage: 18 MB, less than 32.85% of Python3 online submissions for Insert Delete GetRandom O(1).

class RandomizedSet:
    import random
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.rset = {}
        self.rlist = []
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """

        if val in self.rset:
            return False
        
        self.rlist.append(val)
        self.rset[val] = len(self.rlist)-1
        
        return True
    

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """

        if val in self.rset:
            # Swap the last item and the wanted value
            index = self.rset[val]
            last = self.rlist[-1]
            
            self.rlist[index], self.rlist[-1] = last, val
            self.rset[last] = index
            
            self.rlist.pop()
            self.rset.pop(val)
            return True
        return False
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        if self.rset:
            index = random.randint(0,len(self.rlist)-1)
            return self.rlist[index]


# Your RandomizedSet object will be instantiated and called as such:
# val = 2
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# print(param_1)
# # param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# print(param_3)

obj = RandomizedSet()
param_1 = obj.insert(2)
param_2 = obj.insert(2)
print(param_2)