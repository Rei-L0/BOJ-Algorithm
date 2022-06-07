S = input()

alpha = []*26

for i in range(26):
    alpha.append(S.count(chr(i+97)))

for i in alpha:
    print(i, end=' ')
