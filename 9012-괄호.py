T = int(input())

str = []

for i in range(T):
    str.append(list(input()))

    sum = 0

    for j in str[i]:
        if j == '(':
            sum += 1
        elif j == ')':
            sum -= 1

        if sum < 0:
            print('NO')
            break

    if sum > 0:
        print('NO')
    elif sum == 0:
        print('YES')
