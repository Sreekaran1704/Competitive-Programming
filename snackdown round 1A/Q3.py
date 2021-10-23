# cook your dish here
for i in range(int(input())):
    x,k=map(int,input().split())
    print(f"{2*x} {x*k*(x*k-1)}")