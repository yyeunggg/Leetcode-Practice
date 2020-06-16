# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 22:46:20 2020

@author: steve
"""

"""
787. Cheapest Flights Within K Stops
https://leetcode.com/problems/cheapest-flights-within-k-stops/

"""



# Try DP
"""
Runtime: 336 ms, faster than 10.25% of Python3 online submissions for Cheapest Flights Within K Stops.
Memory Usage: 15.3 MB, less than 45.52% of Python3 online submissions for Cheapest Flights Within K Stops
"""
class Solution:
    def findCheapestPrice(self, n, flights, src, dst, K):
        K += 1
        self.dest = dst        

        # Clean data according to my convention
        # So every state is (vertices,stop)
        starts = {}

        for flight in flights:
            if flight[0] not in starts:
                starts[flight[0]] = [(flight[1],flight[2])]
            else:
                starts[flight[0]].append((flight[1],flight[2]))

        self.cost = {}
        
        if src not in starts:
            return -1
        
        def find_next_state(current_city, remain_stop):
            if (current_city,remain_stop) in self.cost:
                return self.cost[(current_city,remain_stop)]
                
            if remain_stop < 0:
                self.cost[(current_city,remain_stop)] = float('inf')
                return float('inf')
            
            if current_city == self.dest:
                self.cost[(current_city,remain_stop)] = 0
                return 0

            if current_city not in starts:
                self.cost[(current_city,remain_stop)] = float('inf')
                return float('inf')
            
            # if (current_city,remain_stop) not in self.cost:
            self.cost[(current_city,remain_stop)] = float('inf')

            for neighbors in starts[current_city]:
                next_city = neighbors[0]
                cost = neighbors[1]
                cost += find_next_state(next_city, remain_stop - 1)
                self.cost[(current_city,remain_stop)] = min(self.cost[(current_city,remain_stop)],cost)
                
            return self.cost[(current_city,remain_stop)]
        
                
        find_next_state(src,K)
        if self.cost[(src,K)] == float('inf'):
            return -1
        return self.cost[(src,K)]


class Solution:
    def findCheapestPrice(self, n, flights, src, dst, K):
        import collections
        from collections import defaultdict
        import heapq
        from heapq import heappop, heappush
        
        graph = defaultdict(list)
        
        for u, v, w in flights:
            graph[u].append((v, w))
            
    
        # dist, idx, path_len
        q = [(0, src, 1)]
        max_path_len = K + 2
        while q:
            print(q)
            dist, idx, path_len = heappop(q)
            # print([dist,idx,path_len])
            if path_len > max_path_len:
                continue
            if idx == dst:
                return dist
            for v, w in graph[idx]:
                heappush(q, (dist+w, v, path_len+1))
        return -1

n = 3
flights = [[0,1,100],[1,2,200],[0,2,300],[2,3,100],[1,3,600],[0,3,500],[0,4,2000],[3,4,100]]
src = 0
dst = 4
K = 5

# n = 3
# flights = [[0,1,100],[1,2,100],[0,2,500]]
# src = 0 
# dst = 2
# K = 1

# n = 5
# flights = [[3,0,8],[1,4,1],[1,0,4],[1,3,3],[3,4,1],[2,3,3],[2,0,10]]
# src = 1
# dst = 4
# K = 4

# n = 17
# flights = [[0,12,28],[5,6,39],[8,6,59],[13,15,7],[13,12,38],[10,12,35],[15,3,23],[7,11,26],[9,4,65],[10,2,38],[4,7,7],[14,15,31],[2,12,44],[8,10,34],[13,6,29],[5,14,89],[11,16,13],[7,3,46],[10,15,19],[12,4,58],[13,16,11],[16,4,76],[2,0,12],[15,0,22],[16,12,13],[7,1,29],[7,14,100],[16,1,14],[9,6,74],[11,1,73],[2,11,60],[10,11,85],[2,5,49],[3,4,17],[4,9,77],[16,3,47],[15,6,78],[14,1,90],[10,5,95],[1,11,30],[11,0,37],[10,4,86],[0,8,57],[6,14,68],[16,8,3],[13,0,65],[2,13,6],[5,13,5],[8,11,31],[6,10,20],[6,2,33],[9,1,3],[14,9,58],[12,3,19],[11,2,74],[12,14,48],[16,11,100],[3,12,38],[12,13,77],[10,9,99],[15,13,98],[15,12,71],[1,4,28],[7,0,83],[3,5,100],[8,9,14],[15,11,57],[3,6,65],[1,3,45],[14,7,74],[2,10,39],[4,8,73],[13,5,77],[10,0,43],[12,9,92],[8,2,26],[1,7,7],[9,12,10],[13,11,64],[8,13,80],[6,12,74],[9,7,35],[0,15,48],[3,7,87],[16,9,42],[5,16,64],[4,5,65],[15,14,70],[12,0,13],[16,14,52],[3,10,80],[14,11,85],[15,2,77],[4,11,19],[2,7,49],[10,7,78],[14,6,84],[13,7,50],[11,6,75],[5,10,46],[13,8,43],[9,10,49],[7,12,64],[0,10,76],[5,9,77],[8,3,28],[11,9,28],[12,16,87],[12,6,24],[9,15,94],[5,7,77],[4,10,18],[7,2,11],[9,5,41]]
# src = 13
# dst = 4
# K = 13


sol = Solution()
print(sol.findCheapestPrice(n,flights,src,dst,K))
        