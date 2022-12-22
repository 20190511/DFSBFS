"""
4 5
00110
00011
11111
00000

15 14
00000111100000
11111101111110
11011101101110
11011101100000
11011111111111
11011111111100
11000000011111
01111111111111
00000000011111
01111111111000
00011111111000
00000001111000
11111111110011
11100011111111
11100011111111
"""

n, m = map(int, input().split())
#dfs로 끝까지 방문해서 아니면 1로 전환
"""
<<피드백>> : map(int, input()) 하면 한 문자씩 쪼갠다.
graph = [[] for _ in range(n)]
for i in range(n):
  s = input()
  for j in range(m):
    graph[i].append(int(s[j]))
"""
graph = []
for i in range (n):
  graph.append(map(int,input()))

result = 0
def dfs (graph, x, y):
  if x>=0 and x<n and y>=0 and y<m:
    v = graph[x][y]
    if v == 0:
      graph[x][y] = 1
      dfs(graph, x-1, y)
      dfs(graph, x, y-1)
      dfs(graph, x+1, y)
      dfs(graph, x, y+1)
  return

result = 0
for x in range (n):
  for y in range(m):
    if graph[x][y] == 0:
      dfs(graph,x,y)
      result += 1
print(result)
      