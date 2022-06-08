E, M, S = map(int, input().split())

e, m, s = 1, 1, 1
year = 1
while True:
    if e == E and s == M and m == S:
        break

    e += 1
    s += 1
    m += 1
    year += 1
    if e == 16:
        e = 1
    if s == 29:
        s = 1
    if m == 20:
        m = 1
print(year)
