#Question code : PROBCAT
for i in range(int(input())):
    x=int(input())
    if x<100:
        print("Easy")
    elif x>=100 and x<200:
        print("Medium")
    elif x>=200 and x<=300:
        print("Hard")