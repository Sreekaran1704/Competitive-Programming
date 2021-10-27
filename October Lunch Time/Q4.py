#Question code : CHEFCAR
for i in range(int(input())):
    n,v=map(int,input().split())
    min_price=0
    max_price=n*(n-1)//2
    if v==1:
        min_price=max_price
    else:
        if v>=n-1:
            min_price=n-1
        else:
            min_price+=v+((n-v)*(n-v+1))//2-1
    print(f"{max_price} {min_price}")