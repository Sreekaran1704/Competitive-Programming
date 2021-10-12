#Question Code NPAIRS
from collections import defaultdict
for i in range(int(input())):
    n = int(input())
    s = list(map(int, list(input())))

    a = defaultdict(int)
    b = defaultdict(int)
    for i in range(n):
        a[s[i]+i] += 1
        b[s[i]-i] += 1
    m1, m2 = 0,0
    for v in a.values():
        m1 += (v*(v-1)//2)
    for v in b.values():
        m2 += (v*(v-1)//2)
    print(m1+m2)
