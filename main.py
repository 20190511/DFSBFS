from itertools import permutations
#1720 ~ 1743
"""
연산자 끼워넣기.
https://www.acmicpc.net/problem/14888
"""
n = int(input())
numList = list(map(int,input().split()))
oper = list(map(int,input().split()))
operList =[]
for i in range(4):
  for j in range(oper[i]):
    operList.append(i)
operSet = list(permutations(operList))

def operating(a,b,oper):
  if oper == 0:
    return a+b
  elif oper == 1:
    return a-b
  elif oper == 2:
    return a*b
  elif oper == 3:
    if (a<0 and b>0) or (a>0 and b<0):
      return (abs(a) // abs(b)) * -1
    else:
      return a // b
  else:
    return

sums = []    
for sets in operSet:
  vals = numList[0]
  for i in range(n-1):
    vals = operating(vals,numList[i+1],sets[i])
  sums.append(vals)

print(max(sums))
print(min(sums))
operSet.clear()
numList.clear()
oper.clear()


"""
-> dfs 방식으로도 풀 수 있다.
  1. 같은 연산자 4개 중 [2,1,1,1] 중 5개를 조합하는 경우
  
"""