from collections import deque
"""
https://www.acmicpc.net/problem/18352 : 최단경로 구하기
#1차 : 이상하게 생각함 (문제이해 실패)
#2110 ~ 2137 시간초과?

4 4 2 1
1 2
1 3
2 3
2 4

4 3 2 1
1 2
1 3
1 4

4 4 1 1
1 2
1 3
2 3
2 4
"""
N, M, K, X = map(int,input().split()) #K거리 도로 찾기
N += 1
city = [[] for _ in range(N)]
path = [-1 for _ in range(N)]
visited = [False for _ in range(N)]
for i in range(M):
  start, end = map(int, input().split())
  city[start].append(end)

queue = deque([X])
path[X] = 0
while queue:
    v = queue.popleft()
    citys = city[v]
    for item in citys:
        if path[item] == -1:
          queue.append(item)
          path[item] = path[v] + 1

#print(path)
count = 0
for i in range(1, N):
  if path[i] == K:
    print(i)
    count +=1
if count == 0:
  print(-1)


  """
  <<피드백>>
    bfs 문제인데, 시간이 빽빽한문제
    
  
    1. 문제를 제대로 읽자 :
      모든 도시를 한 번씩 지나갔을 때, 최단경로 구하기

    2. visited[] 할 때, 시작노드를 0으로 설정하는 것 
      -> path 가 -1 일 때, 한 번도 안 지나간 것, 0이상일때 각 길이를 초기화 시켜준다.

    3. 만약 시간초과가 발생했을 때, def에서 call 하는 방식을 지우고 그냥 넣어보면 돌아갈 때가 많다.
      ++ pypy로 해보자.
  """


  
