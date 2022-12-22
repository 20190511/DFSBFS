from collections import deque
#2210
"""
https://www.acmicpc.net/problem/18428
check함수에서 시간 많이 걸림. <- BFS방식으로 해결
모든 조합(중복조합) 문제는 DFS 방식으로 해결가능
"""
n = int(input())
hall = []
for i in range(n):
  hall.append(list(map(str,input().split())))

teacher = []
student = []
def obj (hall):
  teacher = []
  hallc = len(hall)
  for i in range(hallc):
    for j in range(hallc):
      if hall[i][j] == "T":
        teacher.append([i,j])
  return teacher
teacher = obj(hall)
#print(teacher)

def check(hall, teacher):
  for t in teacher:
    posx, posy = t[0], t[1]
    moving = [[1,0],[-1,0],[0,1],[0,-1]] #down,up,left,right
    queue = deque(moving)
    while queue:
      m = queue.popleft()
      nx,ny = m[0]+posx, m[1]+posy
      if nx<0 or nx>=len(hall) or ny<0 or ny>=len(hall):
        continue
      else:
        if hall[nx][ny] == "X":
          if m[0]<0:
            m[0] -= 1
          elif m[0]>0:
            m[0] += 1
          if m[1]<0:
            m[1] -= 1
          elif m[1]>0:
            m[1] += 1
          queue.append(m)
          continue
        elif hall[nx][ny] == "S":
          return False
  return True
            
bs = False
def dfs (hall, n):
  hallc = len(hall)
  global bs
  if n == 3:
    if check(hall,teacher):
      bs = True
      return
  else:
    for i in range(hallc):
      for j in range(hallc):
        if hall[i][j] == "X":
          hall[i][j] = "O"
          dfs(hall,n+1)
          hall[i][j] = "X"
          

dfs(hall,0)
if bs == True:
  print("YES")
else:
  print("NO")

