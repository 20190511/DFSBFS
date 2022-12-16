from collections import deque
def dfs (graph, start, visited):
    v = graph[start]
    visited[start] = True
    print(start, end=" ")
    for item in v:
        if not visited[item]:
            dfs(graph, item, visited)
            
def initVisted(visited):
    li = visited
    print()
    """
    for item in visited:
        print(item)
        item = False
    """
    for i in range(len(li)):
        li[i] = False

    
def bfs (graph, start, visited):
    queue = deque([start])
    visited[start] = True
    
    while queue:
        n = queue.popleft()
        print (n, end=" ")
        for item in graph[n]:
            if visited[item] == False:
                visited[item] = True
                queue.append(item)
            
            
graph = [
    [], 
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9
dfs(graph, 1, visited)
initVisted(visited)
print()
#print(visited)
bfs(graph, 1, visited)

"""
     for item in visited:
        print(item)
        item = False
    #다음 코드는 오류를 일으킨다!
        -> item 을 변경시키려고 하면 오류발생!
"""