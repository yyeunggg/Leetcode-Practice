# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 23:25:35 2020

@author: steve
"""


"""
1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance
https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/
"""


def findTheCity(n,edges,distanceThreshold):  
    # Process the edge data a little bit. Requires O(E)
    vertices = {}
    d = {}

    for edge in edges:
        if edge[0] in vertices:
            vertices[edge[0]].append(edge[1:])
        else:
            vertices[edge[0]] = [edge[1:]]
            
            
        edge2 = [edge[0],edge[-1]]
        
        if edge[1] in vertices:
            vertices[edge[1]].append(edge2)
        else:
            vertices[edge[1]] = []
            vertices[edge[1]].append(edge2)
                          
    # Initiliaze distance
    que = []
    prev = {}
    
    for vert in vertices:
        d[vert] = float('inf')
        que.append(vert)
    
    next_vert = 0
    d[0] = 0
    
    while que:
        for edge in vertices[next_vert]:
            d_temp = d[next_vert] + edge[1]
            if d[edge[0]] > d_temp:
                d[edge[0]] = d_temp
                prev[edge[0]] = next_vert
                
        que.remove(next_vert)
        
        dis = float('inf')
        for vert in que:
            if dis > d[vert]:
                next_vert = vert
                dis = d[vert]
    # 这一题我审错了，应该用一个d的matrix更好    
    return d

    
    
n = 5
edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]]
distanceThreshold = 2

print(findTheCity(n,edges,distanceThreshold))