N = int(input())

T = [0]*1000
P = [0]*1000

dp = [0]*20

for i in range(N):
    T[i], P[i] = map(int, input().split())

for i in range(N-1, -1, -1):
    if T[i]+i > N:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], P[i]+dp[i+T[i]])
print(dp[0])
