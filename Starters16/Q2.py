#Question Code:- HCAGMAM1
#Code
for i in range(int(input())):
    x,y=map(int,input().split())
    s=input()
    c=0
    for i in s:
        if i=="1":
            c+=1
    a=c*x
    l=s.split("0")
    b=max(l)
    r=y*len(b)
    result=r+a
    print(result)
