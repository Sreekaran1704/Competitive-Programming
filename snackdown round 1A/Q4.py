for _ in range(int(input())):
    n = int(input())
    ans1=0
    ans2=0
    lst = list(map(int, input().split()))[:n]
    lst.sort()
    l=1
    r= n-2
    if n==2:
        print(0)
        continue
    elif n==3:
        print(min(lst[2]-lst[1], lst[1]-lst[0]))
        continue
    for i in range(n-1):
        ans1+=abs(lst[i] - lst[(n-1)//2])
    for i in range(1,n):
        ans2+=abs(lst[i] - lst[1+(n-1)//2])
    m = min(ans1,ans2)
    while l<r:
        d2 = lst[n-1] - lst[l]
        d1 = lst[r] - lst[0]
        m = min(m, abs(d1-d2))
        if d1<d2:
            l+=1
        else:
            r-=1
    print(m)
