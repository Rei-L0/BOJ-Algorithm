import re


T = int(input())


def sol(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    else:
        return sol(n-1)+sol(n-2)+sol(n-3)


for _ in range(T):
    N = int(input())
    print(sol(N))
