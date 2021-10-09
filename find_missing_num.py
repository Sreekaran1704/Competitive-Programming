#Question : Find the Missing number in the integer array
my_list=[1,2,3,5,6,7,8,9,10]
def num(lst,n):
    sum1=(n)*(n+1)/2
    sum2=sum(lst)
    print(sum1-sum2)
num(my_list,10)
