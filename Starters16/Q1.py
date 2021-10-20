#Question code :- PASSORFAIL
for i in range(int(input())):
    n,x,p=map(int,input().split())
    m=(x*3-(n-x))
    if m>=p:
        print("PASS")
    else:
        print("FAIL")