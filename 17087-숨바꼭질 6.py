from math import gcd
from functools import reduce


def find_gcd(list):
    x = reduce(gcd, list)
    return x


n, s = map(int, input().split())

a = list(map(int, input().split()))

d = []

for i in a:
    if i < s:
        d.append(s-i)
    else:
        d.append(i-s)

print(find_gcd(d))
