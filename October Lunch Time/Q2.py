#Question code : ALTER
for i in range(int(input())):
    a,b,p,q=map(int,input().split())
    if p%a==0 and q%b==0:
        x=p/a
        y=q/b
        if x-y==1 or y-x==1 or x-y==0 or y-x==0:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")