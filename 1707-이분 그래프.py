import sys
from collections import deque

T = int(input())


def BFS(graph, start):
    queue = deque()
    queue.append(start)
    if visited[start] == 0:
        visited[start] = 1

    while queue:
        v = queue.popleft()

        color = visited[v]
        for i in graph[v]:
            if visited[i] == 0:
                queue.append(i)
                if color == 1:
                    visited[i] = 2
                else:
                    visited[i] = 1
            elif visited[i] == 1:
                if color == 1:
                    print("NO")
                    return False
            elif visited[i] == 2:
                if color == 2:
                    print("NO")
                    return False
    return True


for _ in range(T):
    V, E = map(int, sys.stdin.readline().rstrip().split())

    graph = [[]for _ in range(V+1)]
    visited = [0]*(V+1)
    res=0

    for _ in range(E):
        a, b = map(int, sys.stdin.readline().rstrip().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1,V+1):
        if not BFS(graph,i):
            res=1
            break
    if res==0:
        print('YES')