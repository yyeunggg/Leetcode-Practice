# -*- coding: utf-8 -*-
"""
Created on Thu May 28 21:55:22 2020

@author: steve
"""

"""

846. Hand of straights
"""

# This one is kind of slow because remove is O(n) and while is O(n)
# def isNStraightHand(hand,W):
    
#     if W == 1:
#         return True
    
#     if len(hand) % W != 0:
#         return False
    
#     hand.sort()
    
#     while hand:
#         number = hand[0]
#         try:
#             for remove_number in range(number,number+W):
#                 hand.remove(remove_number)
#         except:
#             return False
    
#     return True
    

def isNStraightHand(hand,W):
    
    if W == 1:
        return True
    
    if len(hand) % W != 0:
        return False
    
    # It is a O(N+MlogM) operation. M is the number of different cards
    import collections
    count = collections.Counter(hand)

    
    for card in sorted(count):
        if count[card] > 0:
            card_count = count[card]
            for i in range(W):
                count[card+i] -= card_count
                if count[card+i] < 0:
                    return False
    return True
        


    
    

hand = [1,2,3,6,2,3,4,7,8]

W = 3

print(isNStraightHand(hand,W))