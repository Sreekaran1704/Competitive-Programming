#Question Code : SUBTASK
# for i in range(int(input())):
#     n,m,k=map(int,input().split())
#     a=list(map(int,input().split()))
#     c=0
#     for i in range(n):
#         if a[i]==1:
#             c+=1
#         else:
#             break
#     if c==n:
#         print(100)
#     elif c>=m:
#         print(k)
#     else:
#         print(0)
for i in range(int(input())):
    n=int(input())
    a=list(map(int,input()))
    b=list(map(int,input()))
    l=[]
    for i in range(1,n):
        l.append(a[i]-a[i-1])
    c=sum(l)
    count=0
    for i in b:
        c=c-i
        if c>=0:
            count+=1
        else:
            print(count-1)
            break
     
