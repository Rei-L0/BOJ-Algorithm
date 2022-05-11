import sys

N = int(sys.stdin.readline())

stack = []
for _ in range(N):
    com = sys.stdin.readline().split()

    if com[0] == 'push':
        stack.append(com[1])
    elif com[0] == 'pop':
        if not stack:
            print(-1)
        else:
            print(stack.pop())
    elif com[0] == 'size':
        print(len(stack))
    elif com[0] == 'empty':
        if not stack:
            print(1)
        else:
            print(0)
    elif com[0] == 'top':
        if not stack:
            print(-1)
        else:
            print(stack[-1])
