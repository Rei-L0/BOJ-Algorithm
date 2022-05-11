from collections import deque


def BFS(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(8):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y]+1
                if (nx, ny) == (x1, y1):
                    return graph[nx][ny]
                queue.append((nx, ny))


T = int(input())

dx = [2, 2, 1, 1, -1, -1, -2, -2]
dy = [1, -1, 2, -2, 2, -2, 1, -1]

while T != 0:
    N = int(input())
    graph = []
    for _ in range(N):
        graph.append(list(map(int, '1'*N)))
    x, y = map(int, input().split())
    x1, y1 = map(int, input().split())
    graph[x1][y1] = 1

    if (x, y) == (x1, y1):
        print(0)
    else:
        print(BFS(x, y)-1)
    T -= 1
