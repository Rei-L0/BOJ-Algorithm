from collections import deque
import copy


def BFS(x, y, h):
    queue = deque()
    queue.append((x, y))

    while queue:
        a, b = queue.popleft()
        for i in range(4):
            nx = a+dx[i]
            ny = b+dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if data1[nx][ny] >= h:
                data1[nx][ny] = 0
                queue.append((nx, ny))
    return


N = int(input())

data = []

dx = [-1, 0, 0, 1]
dy = [0, 1, -1, 0]

result = []

maxh = 0
for i in range(N):
    data.append(list(map(int, input().split())))
    if max(data[i]) > maxh:
        maxh = max(data[i])

for h in range(maxh+1):
    data1 = copy.deepcopy(data)
    count = 0
    for i in range(N):
        if h == 0:
            result.append(1)
            break
        for j in range(N):
            if data1[i][j] >= h:
                BFS(i, j, h)
                count += 1
    result.append(count)
print(max(result))
