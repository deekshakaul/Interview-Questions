https://leetcode.com/problems/minimum-cost-to-connect-sticks/

import heapq
def minimumCost(sticks):
  heapq.heapify(sticks)
  cost = 0
  while len(sticks)>1:
    smallest=heapq.heappop(sticks)
    second = heapq.heappop(sticks)
    cost+=smallest+second
    heapq.heappush(sticks, (smallest+second))
  return cost


sticks = [1,8,5,3]
sticks.sort()
cost = minimumCost(sticks)
print(cost)
