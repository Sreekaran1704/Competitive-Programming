#Question Code : THREEBOX
#code
for i in range(int(input())):
    a,b,c,d=map(int,input().split())
    if (a + b + c <= d):
        print(1)
    elif (a + b <= d):
        print(2)
    else:
        print(3)
