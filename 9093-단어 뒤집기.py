T = int(input())

str = []

for _ in range(T):
    str.append(list(input().split()))

for i in range(T):
    for j in range(len(str[i])):
        print(str[i][j][::-1], end=' ')
    print()
