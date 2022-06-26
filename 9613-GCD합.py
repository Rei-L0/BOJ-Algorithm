from math import gcd

t = int(input())

for _ in range(t):
    data = list(map(int, input().split()))

    result = 0

    for i in range(1, data[0]+1):
        for j in range(i+1, data[0]+1):
            result += gcd(data[i], data[j])
    print(result)
