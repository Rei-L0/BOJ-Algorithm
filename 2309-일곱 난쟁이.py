a = []
for i in range(9):
    a.append(int(input()))

result = sum(a)
a.sort()
for i in range(len(a)):
    for j in range(i+1, len(a)):
        if a[i]+a[j] == sum(a)-100:
            b = a[i]
            c = a[j]
            a.remove(b)
            a.remove(c)
            break

for i in a:
    print(i)
