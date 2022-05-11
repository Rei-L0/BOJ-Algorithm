from collections import deque


def bfs(graph, a, b):
    N = len(graph)
    queue = deque()
    queue.append((a, b))
    graph[a][b] = 0
    si = 1
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
                si += 1
    return si


N = int(input())

graph = []

for _ in range(N):
    graph.append(list(map(int, input())))


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

size = []

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            size.append(bfs(graph, i, j))

size.sort()
print(len(size))
for i in size:
    print(i)
