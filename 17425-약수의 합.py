import sys

MAX = 1000000
dp = [1]*(MAX+1)

result = [0]*(MAX+1)

for i in range(2, MAX+1):
    j = 1
    while i*j <= MAX:
        dp[i*j] += i
        j += 1

for i in range(1, MAX+1):
    result[i] = result[i-1] + dp[i]

T = int(input())

for _ in range(T):
    a = int(sys.stdin.readline())
    print(result[a])
