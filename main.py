#2030 1차시도 실패
#2210~2240 2차시도 성공
#https://school.programmers.co.kr/learn/courses/30/lessons/60058
"""
1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다. 
2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 
없어야 하며, v는 빈 문자열이 될 수 있습니다. 
3. 문자열 u가 "올바른 괄호 문자열" 이라면 
문자열 v에 대해 1단계부터 다시 수행합니다. 
  3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다. 
4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다. 
  4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다. 
  4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다. 
  4-3. ')'를 다시 붙입니다. 
  4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다. 
  4-5. 생성된 문자열을 반환합니다.
  """
def check(u):
    st = []
    for item in u:
        st.append(item)
        if len(st) > 1:
            if st[-1] != st[-2]:
                if st[-2] == ")":
                    return False
                st.pop()
                st.pop()

        else:
            if st[0] == ")":
                return False
    return True
  
def flip(u):
    news = ""
    for ch in u:
        if ch == "(":
            news += ")"
        else:
            news += "("
    return news

def A (ch):
    if ch == "":
        return ""
    countA, countB = 0,0
    idx = 0
    while True:
        if ch[idx] == "(":
            countA += 1
        else:
            countB += 1
        if countA == countB:
            break
        idx += 1
    sums = countA+countB
    u = ch[0:sums]
    v = ch[sums:]
    if check(u) == True:
        return u+A(v)
    else:
        news = "("+A(v)+")"+flip(u[1:-1])
        return news
    
    

case1 = "(()())()"
case2 = ")("	
case3 = "()))((()"
print(A(case1))
print(A(case2))
print(A(case3))

"""
  <피드백> :
    -> 재귀적으로 푼다고 하면 재귀함수니까 함수 만들어서 풀자!

  [테크닉]
    ( ) 가 짝을 이루어서 짝이 될 때까지 u를 구하는 것이니까
    (갯수와 )갯수가 동일할 때까지 while 돌려서 같아지는 인덱스까지
    u라고 정해놓고 푼 뒤에 나머지는 문제를 잘따라가면서 풀면 해결된다.
    (문제 해독이 오래걸렸는데 예시와 문제를 잘 번갈아보며 풀어보자.)
    
  [실수정리]
    1. a[1:-3] -> a[1] ~ a[-2] 까지 출력한다.
      -> -3번 인덱스까지 출력한다고 생각하지 말자.
    2. string 객체는 append 함수가 없다.
      -> a = b+c 같은 연산을 해주는 것이 바람직하다.
    3. pop 하기 전에 접근해야하는 인덱스가 있는지 생각하자.
    4. 
"""