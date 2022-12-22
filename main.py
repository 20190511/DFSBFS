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

def check(hall, x,y,typex,typey):
  count = 1
  nx,ny = typex*count+x, typey*count+y
  while nx>=0 and nx<len(hall) and ny>=0 and ny<len(hall):
    if hall[nx][ny] == "X":
      count += 1
      nx,ny = typex*count+x, typey*count+y
    elif hall[nx][ny] == "S":
      return True
    else:
      return False
  return False
    
    
bs = True
def dfs (hall, n):
  hallc = len(hall)
  global bs
  if n == 3:
    for t in teacher:
      moving = [[1,0],[-1,0],[0,1],[0,-1]]
      for m in moving:
        if check(hall,t[0],t[1],m[0],m[1]):
          return True #학생 발견하면 True
    bs = False
    return False
  else:
    for i in range(hallc):
      for j in range(hallc):
        if hall[i][j] == "X":
          hall[i][j] = "O"
          dfs(hall,n+1)
          hall[i][j] = "X"
          

dfs(hall,0)
if bs == False:
  print("YES")
else:
  print("NO")

"""
피드백
1. 돌아가는 for 문의 리스트의 값을 함부로 pop하지말것. 
  -> 프로그램이 미친듯이 꼬일것임.
  ex) for item in lista:
        lista.pop() #<- 꼬임의 시초

2. dfs함수는 return값이 일정하지 않을 수 있으므로,
    global 변수를 둬서 처리하면 편하다.

3. 여러 방향을 검사하는 함수를 만들 때, dfs, bfs로 만들기 곤란하다면,
    함수내에서 여러 조건으로 쪼개서 호출하는 것도 한 방법이다.


스킬.
  1. 좌표는 그대로 있는 값을 상하좌우로 n만큼 계속 커지면서 탐색하는 경우
    -> count를 증가시키면서 move*count+현포지션 방식으로 구할 수 있다.
  ex)
  def check(hall, x,y,typex,typey):
  count = 1
  nx,ny = typex*count+x, typey*count+y
  while nx>=0 and nx<len(hall) and ny>=0 and ny<len(hall):
    if hall[nx][ny] == "X":
      count += 1
      nx,ny = typex*count+x, typey*count+y
    elif hall[nx][ny] == "S":
      return True
    else:
      return False
  return False

  2. True-False 방식을 유동적으로 배치하여서,
      만약 한 번이라도 나오면 되는 조건을 검사할 때,
        글로벌 변수값을 변화시키는 방향으로 코드를 짜면 편하다.

"""

