T = int(input())

for _ in range(T):
    M, N, x, y = map(int, input().split())
    a = b = 0
    while True:
        if x+M*a == y+b*N:
            print(x+M*a)
            break
        elif x+M*a > y+b*N:
            b += 1
        else:
            a += 1
        if a == N or b == M:
            print(-1)
            break
