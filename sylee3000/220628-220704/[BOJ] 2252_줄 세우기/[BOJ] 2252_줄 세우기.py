from collections import deque

N, M = map(int, input().split())
indegree = [0] * (N+1)
graph = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    indegree[B] += 1

def topology_sort(graph):
    result = []
    
    q = deque()
    for i in range(1, N + 1):
        if indegree[i] == 0:
            q.append(i)
            
    while q:
        k = q.popleft()
        result.append(k)
        for i in graph[k]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    print(*result)
topology_sort(graph)
