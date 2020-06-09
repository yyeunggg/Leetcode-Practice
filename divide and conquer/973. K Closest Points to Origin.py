# -*- coding: utf-8 -*-
"""
Created on Sat May 30 23:57:57 2020

@author: steve
"""


"""
973. K Closest Points to Origin


"""



#My own implementation
def kClosest(points,K):
    
    dist_list = []
    
    for index,n in enumerate(points):
        dist = n[0]**2 + n[1]**2
        dist_list.append([dist,n])
        
        
    dist_list = sorted(dist_list,key = lambda x: x[0])      #O(nlogn)
    
    answer = []
    
    for i in range(K):
        answer += [dist_list[i][1]]

    return answer
    

# Or we can use heap
def kClosest(points,K):
    
    import heapq
    
    def find_dist(n):
        return n[0]**2 + n[1]**2
    
    max_heap = []
    
    for point in points[:K]:
        heapq.heappush(max_heap,(-find_dist(point),point))      #Form heap, O(k*logk)
    
    for point in points[K:]:
        heapq.heappushpop(max_heap,(-find_dist(point),point))       #Form and update heap, O((n-k)logk)
        
    answer = [point for _,point in max_heap]
    return answer
    


points =  [[3,3],[5,-1],[-2,4],[6,6]]
K = 2
print(kClosest(points,K))