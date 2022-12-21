from itertools import permutations
#1720 ~ 1743
"""
연산자 끼워넣기.
https://www.acmicpc.net/problem/14888

#2. DFS 방식으로의 풀이
"""
n = int(input())
data = list(map(int, input().split()))
add,sub,mul,div = map(int,input().split())

min_value = 1e9
max_value = -1e9

def dfs(i, now):
  #재귀호출을 하여도 사용할 것이므로 global 선언
  global min_value, max_value, add, sub, mul ,div

    # 모든 연산을 수행한 경우.
  if i == n:
    min_value = min(min_value, now)
    max_value = max(max_value, now)
  else:
    if add > 0:
      add -= 1
      dfs(i+1, now+data[i])
      add += 1
    if sub > 0:
      sub -= 1
      dfs(i+1, now-data[i])
      sub += 1
    if mul > 0:
      mul -= 1
      dfs(i+1, now*data[i])
      mul += 1
    if div > 0:
      div -= 1
      dfs(i+1, int(now/data[i]))
      div += 1


dfs(1, data[0])
print(max_value)
print(min_value)


"""
-> dfs 방식으로도 풀 수 있다.
  ※ DFS 방식 풀이의 예시.
    병렬적으로 모든 경우의수 마다 reculsive-call을 해준다.
    ex) add -= 1 -> 재귀함수호출(i+1,now) -> add += 1
      과 같은 방식을 병렬적으로 수행하면 이 문제를 풀 수 있다.

  [문법]
   1. 함수 내에서의 global 선언 예시
   ※ global 을 함수 내에서 선언하면, 전역변수처리되며
   이전에 들어간 해당 변수값을 계속 사용할 수 있다.
    sum = 3
    def test():
        global sum
        sum += 2
    test()
    print (sum)
    >>> 5

  2. 1억을 표현하는 방법으로 1e9 = 10^9 로 표현할 수 있다.
"""