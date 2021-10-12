#Question Code : SUBTASK
for i in range(int(input())):
    n,m,k=map(int,input().split())
    a=list(map(int,input().split()))
    c=0
    for i in range(n):
        if a[i]==1:
            c+=1
        else:
            break
    if c==n:
        print(100)
    elif c>=m:
        print(k)
    else:
        print(0)
