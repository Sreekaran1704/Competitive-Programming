#Question code : N1VALUES
for i in range(int(input())):
    n=int(input())
    l=[1]
    for i in range(1,n):
        l.append(i)
    n1=2**n
    a=n1-sum(l)
    l.append(a)
    for i in l:
        print(i,end=" ")
    print()