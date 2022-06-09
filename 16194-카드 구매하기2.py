N = int(input())

P = [0]+list(map(int, input().split()))

dp = P

for i in range(1, N+1):
    for j in range(1, i+1):
        dp[i] = min(dp[i], dp[i-j] + P[j])

print(dp[N])
