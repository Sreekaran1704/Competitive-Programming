#Question code-BININVER
for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    e=0
    o=0
    for i in a:
        if i%2==0:
            e+=1
        else:
            o+=1
    if e==n:
        ans=1e9
        for i in range(1,n):
            crr=0
            while(a[i]%2!=1):
                a[i]=a[i]/2
                crr+=1
            if crr<ans:
                ans=crr
        print(ans)
    else:
        print(0)
