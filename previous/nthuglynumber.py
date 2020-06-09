# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 23:04:31 2019

@author: steve
"""



"""

idea from here:
    
    https://leetcode.com/problems/ugly-number-iii/discuss/387539/cpp-Binary-Search-with-picture-and-Binary-Search-Template
    
F(N) = (total number of positive integers <= N which are divisible by a or b or c.) 
    
F(N) = N/a + N/b + N/c - N/lcm(a, c) - N/lcm(a, b) - N/lcm(b, c) + N/lcm(a, b, c)(lcm = least common multiple)
"""
def nthUglyNumber(n: int, a: int, b: int, c: int) -> int:
      
    #Generate a number for binary search, and then do binary search
    
    #Define the LCM function
    import math
    def lcm(a,b):  ###This is how to get LCM！！！
        lcm_value = a*b // math.gcd(a,b)
        return lcm_value
    
    lo = 1
    hi = min([a,b,c]) * n
    
    
    mid = (lo+hi)//2
    
    def fuck(mid, a,b,c):
        FN = mid//a + mid//b + mid//c - mid//lcm(a,b)- mid//lcm(c,b)- mid//lcm(a,c) + mid//lcm(a,lcm(b,c))
        return FN
    
    while fuck(mid,a,b,c) != n-1:
        if fuck(mid,a,b,c) < n -1:
            lo = mid
        else:
            hi = mid
        mid = (lo+hi)//2
        
        
    while fuck(mid,a,b,c) != n:
        mid += 1
    return mid
    


#n = 3, a = 2, b = 3, c = 5
#n = 4, a = 2, b = 3, c =5
    
#n = 1000000000, a = 2, b = 217983653, c = 336916467 
a = nthUglyNumber(n = 4, a = 2, b = 3, c =4)
print(a)