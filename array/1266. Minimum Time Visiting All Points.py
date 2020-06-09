# -*- coding: utf-8 -*-
"""
Created on Tue May 26 15:10:10 2020

@author: steve
"""

"""
1266. Minimum Time Visiting All Points
"""

"""
On a plane there are n points with integer coordinates points[i] = [xi, yi]. Your task is to find the minimum time in seconds to visit all points.

You can move according to the next rules:

In one second always you can either move vertically, horizontally by one unit or diagonally (it means to move one unit vertically and one unit horizontally in one second).
You have to visit the points in the same order as they appear in the array.
"""

# Solution 1 Using list, faster
def minTimeToVisitAllPoints(points):
    # find maximum difference in delx or dely
    time_tot = 0
    for point_index in range(len(points)-1):
        point1 = points[point_index]
        point2 = points[point_index+1]
        del1 = abs(point1[0] - point2[0])
        del2 = abs(point1[1] - point2[1])
        time_dif = max(del1,del2)
        time_tot += time_dif
    return time_tot

# Solution 2, using numpy, but slower
# def minTimeToVisitAllPoints(points):
    # # find maximum difference in delx or dely
    # import numpy as np
    # time_tot = 0
    # for point_index in range(len(points)-1):
    #     point1 = np.array(points[point_index])
    #     point2 = np.array(points[point_index+1])
    #     time_dif = np.amax(np.abs(point1-point2))
    #     time_tot += time_dif
    # return time_tot



points = [[1,1],[3,4],[-1,0]]
print(minTimeToVisitAllPoints(points))