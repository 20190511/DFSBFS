from collections import deque
def picture (graph):
  print("-------------------------------------")
  for i in range(len(graph)):
    for j in range(len(graph[i])):
      print(graph[i][j], end="   ")
    print()
  print("-------------------------------------")
"""
미로탈출 p.152
5 6
101010
111111
000001
111111
111111

12 8
11000111
11110111
00010111
11110000
00100000
01100000
11000000
11110000
00011100
11110000
10000000
11111111
"""
n, m = map(int, input().split())
miro = []
for i in range(n):
  miro.append(list(map(int,input())))

def bfs(graph,n,m):
  queue = deque([[0,0]])
  #상하좌우
  move = [(1,0), (-1,0), (0,1), (0,-1)]
  while queue:
    print(queue), picture(graph)
    info = queue.popleft()
    qx, qy = info[0], info[1]
    if qx == n-1 and qy == m-1:
      break
    for mo in move:
      nx, ny = qx+mo[0],qy+mo[1]  #qy+mo[1] 를 qx+mo[1] 로 해버리는 실수를 하였다 허허.
      if nx < 0 or nx >= n or ny<0 or ny>=m:
        continue
      if graph[nx][ny] == 0:
        continue
      if graph[nx][ny] == 1:
        queue.append([nx,ny])
        graph[nx][ny] = graph[qx][qy] + 1
  return graph[n-1][m-1]

#print(bfs(miro,n,m))


"""
<<피드백>>
 ★ graph의 총 길이를 구하고 싶은 경우,
    :graph[qn][ny] = graph[qx][qy] + 1
    과 같이 이전의 그래프의 값에서 1을 더해주면 된다.
      ※[0,0]의 값은 원래 1이기 때문에 이 문제의 경우에는 값이 계속 바뀔 수 있다. 
        (마지막에 grpah[0][0] = 1) 을 해주면 된다.
      ※경로 찾기의 경우, result 값으로 시작하여 그 값의 -1 값을 queue에 넣고 
        상하좌우 중에 1씩 커지는 값을 역추적해가면 된다. 

 1. 경로 길이가 같은 미로 문제의 경우, bfs 이론으로 풀면 쉽다.
 2. 혹시라도, deque() 에 값을 넣을 때에는,
    변수 하나인 경우 deque([1])
    리스트의 경우 deque([[1,2]]) 
    이런식으로 넣어줘야 한다.

3. 아래와 같이 더 짧은 코드로도 문제를 수행할 수 있다.


"""


def bfs2(graph,n,m):
  queue = deque([[0,0]])
  #상하좌우
  move = [(1,0), (-1,0), (0,1), (0,-1)]
  while queue:
    print(queue), picture(graph)
    info = queue.popleft()
    qx, qy = info[0], info[1]
    graph[0][0] = 2
    if qx == n-1 and qy == m-1:
      break
    for mo in move:
      nx, ny = qx+mo[0],qy+mo[1]  #qy+mo[1] 를 qx+mo[1] 로 해버리는 실수를 하였다 허허.
      if nx >= 0 and nx < n and ny>=0 and ny<m:
        if graph[nx][ny] == 1:
          queue.append([nx,ny])
          graph[nx][ny] = graph[qx][qy] + 1
  return graph[n-1][m-1]-1

#print(bfs2(miro,n,m))
def navigate (graph):
  n = len(graph)
  m = len(graph[0])
  print(n,m)
  start = [[n-1,m-1]]
  navi = []
  move = [(0,1),(0,-1),(1,0),(-1,0)]
  while True:
    qx, qy = start[0][0], start[0][1]
    val = graph[qx][qy]
    #print(start, val)
    start.pop(0)
    if qx == 0 and qy == 0:
      break
    for mo in move:
      nx,ny = qx+mo[0], qy+mo[1]
      if nx>=0 and nx<n and ny>=0 and ny<m:
        if graph[nx][ny] == val-1:
          start.append([nx,ny])
        navi.pop()
  return navi

bfs2(miro,n,m)
print(navigate(miro))

    