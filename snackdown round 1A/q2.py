# cook your dish here
t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    ans=(2*n-k-1)//2
    print(2*ans)