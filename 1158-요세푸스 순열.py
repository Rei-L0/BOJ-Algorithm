a, b = map(int, input().split())

c = [i for i in range(1, a+1)]

d = []
j = b-1

for _ in range(a):
    tmp_len = len(c)
    while j >= tmp_len:
        j -= tmp_len
    d.append(c[j])
    del c[j]
    j += b-1

print('<' + str(d)[1:-1] + '>')
