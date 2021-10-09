#Question code  ADDNDIV
import math
for i in range(int(input())):
    a,b=map(int,input().split())
    c=math.gcd(a,b)
    d=a//c
    if pow(b,d,a)==0:
        print("YES")
    else:
        print("NO")
