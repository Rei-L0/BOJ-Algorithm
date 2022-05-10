import sys
from collections import deque
sys.setrecursionlimit(10**5)

input = sys.stdin.readline

T = int(input())

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(graph, x, y):

    queue = deque()
    queue.append((x, y))
    graph[x][y] = 0

    while queue:
        a, b = queue.popleft()
        for i in range(4):
            nx = a+dx[i]
            ny = b+dy[i]
            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
    return


while T != 0:
    count = 0
    M, N, K = map(int, input().split())
    graph = [[0]*N for _ in range(M)]

    for _ in range(K):
        a, b = map(int, input().split())
        graph[a][b] = 1

    for i in range(M):
        for j in range(N):
            if graph[i][j] == 1:
                bfs(graph, i, j)
                count += 1

    print(count)
    T -= 1
