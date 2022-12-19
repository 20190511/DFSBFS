"""
https://www.acmicpc.net/problem/18405
경쟁적 점염 : 우선순위에 맞게 queue에 삽입
"""
from collections import deque
#queue에 1~K 다 넣고시작
n, k = map(int, input().split())
graph = []
timeGraph = [[0]*n for _ in range(n)]
for i in range(n):
  graph.append(list(map(int,input().split()))) 
time,X,Y = map(int, input().split())


def virusI ():
  queue = deque()
  for x in range(1, k+1):
    for i in range(n):
      for j in range(n):
        if graph[i][j] == x:
          queue.append([i,j])
  return queue

virusList = virusI()

move = [(0,1),(0,-1),(1,0),(-1,0)]

while virusList:
  a = virusList.popleft()
  dx = a[0]
  dy = a[1]
  type = graph[dx][dy]
  for moving in move:
    nx = dx+moving[0]
    ny = dy+moving[1]
    if nx>=0 and nx<n and ny>=0 and ny<n:
      if graph[nx][ny] == 0:
        graph[nx][ny] = type
        timeGraph[nx][ny] = timeGraph[dx][dy] + 1
        virusList.append([nx,ny])

if timeGraph[X-1][Y-1]>time:
  print(0)
else:
  print(graph[X-1][Y-1])