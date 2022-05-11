from collections import deque
from inspect import stack


def DFS(v, num):
    num += 1
    visited[v] = True

    if v == Y:
        count.append(num)

    for i in graph[v]:
        if not visited[i]:
            DFS(i, num)


N = int(input())

X, Y = map(int, input().split())

T = int(input())

count = []

graph = [[] for _ in range(N+1)]

visited = [False]*(N+1)

for _ in range(T):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

DFS(X, 0)

if len(count) == 0:
    print(-1)
else:
    print(count[0]-1)
