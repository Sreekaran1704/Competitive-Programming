#Taking the number of test cases
#Codechef
#Q1
#Question code:- CLIPLX
for i in range(int(input())):
    x,y=map(int,input().split())
    if x-y>0:
        print(0)
    else:
        print(x-y)
