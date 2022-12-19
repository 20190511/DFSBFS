#30분컷 itertools 에서 combinations 주의
"""
문제 : https://www.acmicpc.net/problem/14502

리스트 복사할 때, 이중 리스트를 복사해야하는 경우
a = b.copy()
for i in range(행):
  a[i] = b[i].copy() 

를 해줘야 깊은 복사가된다.

"""

from itertools import combinations
from collections import deque

n,m = map(int, input().split())
graph = []
for i in range(n):
  graph.append(list(map(int,input().split())))


def wallAndVirus(graph,n,m):
  list0 = []
  virus = []
  for i in range (n):
    for k in range(m):
      if graph[i][k] == 0:
        list0.append([i,k])
      elif graph[i][k] == 2:
        virus.append([i,k])
  comb = list(combinations(list0, 3)), virus
  
  return comb


walls, virus = wallAndVirus(graph,n,m)
move = [(0,1), (0,-1), (1,0), (-1,0)]
#print(virus)

valueList= []
for item in walls:
  newGraph = graph.copy()
  for i in range (n):
    newGraph[i] = graph[i].copy()
  newGraph[item[0][0]][item[0][1]] = 1
  newGraph[item[1][0]][item[1][1]] = 1
  newGraph[item[2][0]][item[2][1]] = 1
  
  for vir in virus:
    queue = deque([vir])
    while queue:
      dn = queue.popleft()
      x = dn[0]
      y = dn[1]
      for moving in move:
        nx = moving[0] + x
        ny = moving[1] + y
        if nx>=0 and nx<n and ny>=0 and ny<m:
          if newGraph[nx][ny] == 0:
            newGraph[nx][ny] = 2
            queue.append([nx,ny])
  count = 0
  for a in range(n):
    for b in range(m):
      if newGraph[a][b] == 0:
        count += 1
  valueList.append(count)

value = max(valueList)
print(value)