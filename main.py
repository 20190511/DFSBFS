from collections import deque
"""
블록이동하기.
https://school.programmers.co.kr/learn/courses/30/lessons/60063

board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]

"""
def rotateRobot(board, pos,st0,st1):
  head,tail,time = pos[0],pos[1],pos[2]
  rotate=[]
  if head[0] == tail[0]:
    sets =  [[head[0],head[1]],[tail[0],tail[1]],[head[0],head[1]],[tail[0],tail[1]]]
    want =  [[head[0]-1,head[1]],[tail[0]-1,tail[1]],[head[0]+1,head[1]],[tail[0]+1,tail[1]]]
    check = [[tail[0]-1,tail[1]],[head[0]-1,head[1]],[tail[0]+1,tail[1]],[head[0]+1,head[1]]]
    for i in range (4):
      if 0<=want[i][0]<len(board):
        if board[want[i][0]][want[i][1]]!=1 and board[check[i][0]][check[i][1]]!=1:
          xs,ys = (want[i][0]+sets[i][0])//2,(want[i][1]+sets[i][1])//2
          if not st1[xs][ys]:
            st1[xs][ys] = True
            rotate.append([sets[i],want[i],time+1,1])
  else: #세로
    sets =  [[head[0],head[1]],[tail[0],tail[1]],[head[0],head[1]],[tail[0],tail[1]]]
    want =  [[head[0],head[1]-1],[tail[0],tail[1]-1],[head[0],head[1]+1],[tail[0],tail[1]+1]]
    check = [[tail[0],tail[1]-1],[head[0],head[1]-1],[tail[0],tail[1]+1],[head[0],head[1]+1]]
    for i in range (4):
      if 0<=want[i][1]<len(board):
        if board[want[i][0]][want[i][1]]!=1 and board[check[i][0]][check[i][1]]!=1:
          xs,ys = (want[i][0]+sets[i][0])//2,(want[i][1]+sets[i][1])//2
          if not st0[xs][ys]:
            st0[xs][ys] = True
            rotate.append([sets[i],want[i],time+1,0])
  return rotate

def solution(board):
  robot = deque([[[0,0],[0,1],0,0]]) #위치, 시간, 상태 0:가로, 1:세로
  move = [[0,1],[0,-1],[1,0],[-1,0]]
  state1 = [[False]*len(board) for _ in range(len(board)-1)]
  state0 = [[False]*(len(board)-1) for _ in range(len(board))]
  bl = len(board)
  state0[0][0] = True #시작.
  
  while robot:
    one = robot.popleft()
    pos1, pos2, ts, st = one[0],one[1],one[2],one[3]
    if pos1[0]==bl-1 and pos1[1]==bl-1:
      return ts
    if pos2[0]==bl-1 and pos2[1]==bl-1:
      return ts
    for a,b in move:
      dx1, dy1 = pos1[0]+a,pos1[1]+b
      dx2, dy2 = pos2[0]+a,pos2[1]+b
      if 0<=dx1<bl and 0<=dx2<bl and 0<=dy1<bl and 0<=dy2<bl:
        if board[dx1][dy1]!=1 and board[dx2][dy2]!=1:
          xs,ys = (dx1+dx2)//2,(dy1+dy2)//2
          if st == 0:
            if not state0[xs][ys]:
              state0[xs][ys] = True
              robot.append([[dx1,dy1],[dx2,dy2],ts+1,st])
          else:
            if not state1[xs][ys]:
              state1[xs][ys] = True
              robot.append([[dx1,dy1],[dx2,dy2],ts+1,st])
    
    rots = rotateRobot(board,one,state0,state1)
    if len(rots)>= 1:
      for e in rots:
        robot.append(e)
  return 







board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]
board2= [[0, 0, 0, 0, 0, 0],[0, 0, 0, 1, 1, 1],[0, 0, 1, 1, 1, 1],[0, 0, 1, 1, 1, 1],[0, 0, 0, 0, 0, 0],[0,0,0,0,0,0]]
print(solution(board2))


"""
피드백
1. 코드 복사 붙여넣기 할 때, 세로방향인지 가로방향인지
  비교연산하는 부분 실수함. (아래 코드 유심히 잘 보기.)
      if 0<=want[i][1]<len(board):
2. state 리스트 만들 때, 어떤 state인지 잘 확인하면서 짤 것

괜찮게 푼 방식
 : 경로 시간을 큐에 넣어서 데이터를 꼬리를 무는 형태로 설계

풀이 방식 업그레이드
1. 방문처리 방식
 경계선 처리방식 -> 튜플 (집합) 이용
 ex) next_pos 집합으로 데이터셋을 꾸린 후 
  visited 리스트 안에 해당 값이 있는지 체크한 후 append.

2. 경계처리 대신, 외곽에 벽을 세워서 N+1 배열을 만들면
  처리하기 쉽다

3. deque 에서 다수의 값을 연결하고 싶으면
  deque.extend() 를 사용하라
"""
