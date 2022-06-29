from collections import deque
import sys


def BFS(zido, x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        a, b = queue.popleft()
        for i in range(9):
            nx = a+dx[i]
            ny = b+dy[i]
            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                continue
            if zido[nx][ny] == 1:
                zido[nx][ny] = 0
                queue.append((nx, ny))
    return


while True:

    w, h = map(int, sys.stdin.readline().split())

    if w == 0 and h == 0:
        break

    count = 0
    zido = []

    dx = [-1, -1, -1, 0, 0, 0, 1, 1, 1]
    dy = [1, 0, -1, 1, 0, -1, 1, 0, -1]

    for _ in range(h):
        zido.append(list(map(int, sys.stdin.readline().split())))

    for i in range(h):
        for j in range(w):
            if zido[i][j] == 1:
                BFS(zido, i, j)
                count += 1

    print(count)
