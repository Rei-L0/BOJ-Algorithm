import sys
from collections import deque
sys.setrecursionlimit(5000)


def DFS(v):
    visited[v] = True
    print(v, end=' ')

    for i in graph[v]:
        if not visited[i]:
            DFS(i)


def BFS(V):
    queue = deque([V])

    visited[V] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


input = sys.stdin.readline

N, M, V = map(int, input().split())

graph = [[]for _ in range(N+1)]
visited = [False]*(N+1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(N+1):
    graph[i].sort()

DFS(V)
visited = [False]*(N+1)
print()
BFS(V)
