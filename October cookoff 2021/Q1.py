#Question code : ODDSUM
import sys
input=sys.stdin.readline
for i in range(int(input())):
    n=int(input())
    p=n
    if p<=1:
        sys.stdout.write(str(p)+"\n")
    elif p==2:
        sys.stdout.write(str(1)+"\n")
    elif p==3:
        sys.stdout.write(str(3)+"\n")
    elif p>3:
        sys.stdout.write(str(1+(n-1)*(n-2))+"\n")
