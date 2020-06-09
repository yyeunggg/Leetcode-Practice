# -*- coding: utf-8 -*-
"""
Created on Thu May 28 20:52:37 2020

@author: steve
"""

"""

1366. Rank Teams by Votes


"""


def rankTeams(votes):
    rank = {}
    empty_rank = [0]*len(votes[0])
    answer = ''
    
    
    # First initiate with Alphabetical order
    teams =  votes[0]
    teams = sorted(teams)
    for team in teams:
        rank[team] = empty_rank.copy()  #Remember! Don't change empty rank
        
    # For every vote
    for vote in votes:
        for index, team in enumerate(vote):              
            rank[team][index] += 1

    rank_output = sorted(rank,key = rank.get,reverse = True)
   
    # Concatenate answer
    for team in rank_output:
        answer += team
        
    return answer



# votes = ["ABC","ACB","ABC","ACB","ACB"]
# votes = ["WXYZ","XYZW"]
# votes = ["M","M","M","M"]
votes = ["BCA","CAB","CBA","ABC","ACB","BAC"]
print(rankTeams(votes))