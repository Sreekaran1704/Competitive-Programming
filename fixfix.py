#Question code-FIXFIX
for i in range(int(input())):
    n,k=map(int,input().split())
    if n-k==1:
        print(-1)
    elif n==k:
        for i in range(1,n+1):
            print(i,end=" ")
    else:
        for i in range(1,k+1):
            print(i,end=" ")
        for i in range(k+2,n+1):
            print(i,end=" ")
        print(k+1)
