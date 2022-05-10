def num(x):
    x.sort()
    count = 0
    for i in range(4):
        if x[i]+1 == x[i+1]:
            count += 1
    return count


def color(x):
    x = list(set(x))

    if len(x) == 1:
        return True
    else:
        return False


c = []
n = []

for i in range(5):
    a, b = input().split()
    c.append(a)
    n.append(int(b))
    n.sort()

if color(c) and num(n) == 4:  # 1
    print(900+max(n))
elif n.count(n[0]) == 4:  # 2
    print(800+n[0])
elif n.count(n[1]) == 4:  # 2
    print(800+n[1])
elif n.count(n[1]) == 3 and n.count(n[3]) == 2:  # 3
    print(700+10*n[1]+n[3])
elif n.count(n[1]) == 2 and n.count(n[3]) == 3:  # 3
    print(700+10*n[3]+n[1])
elif color(c):  # 4
    print(600+max(n))
elif num(n) == 4:  # 5
    print(500+max(n))
elif n.count(n[2]) == 3:  # 6
    print(400+n[2])
elif n.count(n[1]) == 2 and n.count(n[3]) == 2:  # 7
    if n[1] > n[3]:
        print(300+10*n[1]+n[3])
    else:
        print(300+10*n[3]+n[1])
elif n.count(n[0]) == 2 or n.count(n[1]) == 2 or n.count(n[2]) == 2 or n.count(n[3]) == 2:  # 8
    for i in range(5):
        if n.count(n[i]) == 2:
            print(200+n[i])
            break
else:  # 9
    print(100+max(n))
