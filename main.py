n, m = map(int, input().split())
data = [] #원본
temp = [[0]*m for _ in range(n)] #벽 설치하고 맵리스트.
for _ in range(n):
  data.append(list(map(int, input().split())))

dx = [-1,0,1,0]
dy = [0,1,0,-1]

result = 0
""" 위의 변수들은 모두 전역변수 취급되어 매개변수로 넣어주지 않아도 작동할 수 있다. 
  카카오 같은 코테는 함수 내에서 함수를 채우는 방식이므로 위 방식을 추천하진 않는다.
  """


#dfs 방식으로 상하좌우로 바이러스를 퍼뜨려준다.
def virus(x,y):
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx>=0 and nx<n and ny>=0 and ny<m:
      if temp[nx][ny] == 0:
        temp[nx][ny] = 2
        virus(nx,ny)

def getScore():
  score = 0
  for i in range(n):
    for j in range(m):
      if temp[i][j] == 0:
        score += 1
  return score


def dfs(count):
  """ ★ global 변수를 설정해서 재귀함수여도 변수가 유지될 수 있도록 할 수 있는 방식! """
  global result   #result 를 global로 선언
  #울타리가 3개인 경우
  if count == 3:
    #temp 리스트 리셋.
    for i in range (n):
      for j in range (m):
        temp[i][j] = data[i][j]

    for i in range(n):
      for j in range(m):
        if temp[i][j] == 2:
          virus(i,j)
      #Score 계산 값과 비교. 후 return(멈추기)
    result = max(result, getScore())
    return

  """ 조합 대신 dfs로 호출하는 방식!"""
  for i in range(n):
    for j in range(m):
      if data[i][j] == 0:
        data[i][j] = 1
        count += 1
        dfs(count)
        #되돌아오면, 원본 복호화 후, count-1
        data[i][j] = 0
        count -= 1

dfs(0)
print(result)

"""
장점 : 아무 것도 import 하지 않았다.
메커니즘 ->
  조합으로 64C3 으로 풀 수 있지만,
    dfs(count) ... 후에 이중 for문으로 벽을 하나씩 세워서
    재귀호출한 뒤 이 리스트가 울타리를 3개를 세웠는지 판단 한 후
    dfs 호출로 문제를 풀면 풀 수 있다.

<<피드백>>
  1. global 선언을 하면, 재귀함수가 호출되는 도중에도 전역변수화 처리되어
    공유하면서 사용할 수 있다.
  2. 리스트복사 .copy는 행 단위로 시행되며 2중리스트 이상되면
    a = b.copy()
    for i in range(행):
      a[i] = b[i].copy() 를 해주던가 n,m for문 돌려서 리셋해주면된다.

  3. deepcopy() 함수 (import copy)
    import copy
    b = copy.deepcopy(a) 를 쓰면 한 줄만에 사용할 수 있긴하다.



"""