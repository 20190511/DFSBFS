#1909 ~ 2018
#https://www.acmicpc.net/problem/16234
from collections import deque
n, small,big = map(int,input().split())
people = []
for i in range(n):
  people.append(list(map(int,input().split())))

def bfsMoving (people):
  clan = [[0]*n for _ in range(n)]
  move = [(1,0),(-1,0),(0,1),(0,-1)]
  sums =[]
  count = 0
  sums.append(0)
  for i in range (n):
    for j in range(n):
      if clan[i][j] == 0:
        count += 1
        queue = deque([[i,j]])
        sums.append(0)
        clan[i][j] = count
        crt = 1
        while queue:
          ct = queue.popleft()
          dx,dy = ct[0],ct[1]
          curr = people[dx][dy]
          sums[count] += curr
          for mx,my in move:
            nx,ny = dx+mx,dy+my
            if nx>=0 and nx<n and ny>=0 and ny<n:
              near = people[nx][ny]
              if clan[nx][ny] == 0:  #조건 추가 실수. : 다음 인접값이 0 이 맞는가 여부 판단.
                if abs(curr-near)>=small and abs(curr-near)<=big:
                  clan[nx][ny] = count
                  queue.append([nx,ny])
                  crt += 1
        sums[count] = sums[count]//crt
  return clan, sums,count

def alu(people,clan,sums):
  for i in range(n):
    for j in range(n):
      people[i][j] = sums[clan[i][j]]

clan, sums,count = bfsMoving(people)
alu(people, clan, sums)
result = 0
while count != n*n:
  result += 1
  clan, sums,count = bfsMoving(people)
  if count == n*n:
    break
  alu(people, clan, sums)
print(result)

"""
<피드백>
 1. 단일 리스트로 생성 시
  a = [False] * 8 이런식으로 해야한다.

 2. visited 조건부 추가를 안하는 실수하였음.
  -> BFS 풀 때 visited 조건을 잘 생각하면서 풀 것.

 해설지 풀이 동일 !

 <새로운 테크닉>
  1. 2차원 리스트 for 문에 대한 고급기술
  move = [[1,0],[-1,0],[0,1],[0,-1]]
  for dx,dy in move: # <- 열 개수만큼 변수를 쓰면 해당 값으로 사용가능.
    nx,ny = dx+x,dy+y 형태로 사용 가능

  2. if 조건 범위 설정 (한꺼번에 설정 가능)
  if 0<=nx<len(people) and 0<=ny<len(people):
"""