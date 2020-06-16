# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 22:19:56 2020

@author: steve
"""

"""
1227. Airplane Seat Assignment Probability
https://leetcode.com/problems/airplane-seat-assignment-probability/
"""

## It's a matter of how he writes the question!!! OMG, finally understood it.
class Solution:
    def nthPersonGetsNthSeat(self,n):
        if n == 1:
            return 1

        prob = 1
        remain_seat = n
        while remain_seat > 1:
            print(remain_seat)
            prob *= (remain_seat - 1)/(remain_seat)
            remain_seat -= 1
            print(prob)
        
        return prob
                

###OK, let's do it, the below will be correct
"""
Let us suppose n>1
Now let us suppose first person goes and sits on k position. Now we surely know that person(2 to k-1) will sit on their correct position(Because when person 2 to k-1 comes then they will find their place empty and will sit on their respective seats). Now k'th person has 3 choices

Sit on seat 1 in which case last person will surely sit on his seat.
Sit on last seat in which case last person will surely not sit on his seat.
Sit on some seat from k+1 to n-1.
Now if he takes option 3 then he will sit on some seat say "j". Now j will again have three options to sit.
This cycle will continue and every person can sit on first and last seat will equal probability. Hence the probability will be 0.5
https://leetcode.com/problems/airplane-seat-assignment-probability/discuss/411905/It's-not-obvious-to-me-at-all.-Foolproof-explanation-here!!!-And-proof-for-why-it's-12
"""
class Solution:
    def nthPersonGetsNthSeat(self,n):
        if n == 1:
            return 1
        
        else:
            return 0.5
                

"""
let's try to solve with DP tomorrow

Reason: 1/n chance aligned with seat -- Success
(n-2)/n chance to get to a smaller window, whose success rate is calculated before
"""
class Solution:
    def nthPersonGetsNthSeat(self,n):
        def find_prob(n):
            if n == 1:
                return 1
            if n == 2:
                return 0.5
            else:
                return 1/n + (n-2)/n*find_prob(n-1)
        
        ans = find_prob(n)
        return ans
        

n = 4
sol = Solution()
print(sol.nthPersonGetsNthSeat(n))
        