n = (1000000)
prime = [True]*n
m = int(n**0.5)
for i in range(2, m+1):
    if prime[i] == True:
        for j in range(i+i, n, i):
            prime[j] = False

while True:
    N = int(input())

    if N == 0:
        break

    for i in range(3, N, 2):
        if prime[i] == True:
            if prime[N-i] == True:
                print(f'{N} = {i} + {N-i}')
                break
        if i == N//2:
            print('"Goldbach\'s conjecture is wrong."')
