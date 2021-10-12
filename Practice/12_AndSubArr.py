#Question Code : ANDSUBAR
def setbits(n):
    ans=0
    while n>0:
        ans+=1
        n=n>>1
    return ans
for i in range(int(input())):
    N=int(input())
    n=setbits(N)
    ans1 = N - (2**(n - 1)) + 1
    ans2 = 2**(n - 1) - 2**(n - 2)
    print(max(ans1,ans2))
