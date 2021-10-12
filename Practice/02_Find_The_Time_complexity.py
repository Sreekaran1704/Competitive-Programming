def printorderpairs(array):
  for i in range(array):
    for j in range(i+1,len(array)):
      print(array[i]+";"+array[j])
      
      
#solution is :First consider the inner loop then
#T(N)=(n-1)+(n-2)+(n-3)+(n-4)+......+3+2+1
#T(N)=(n-1)(n)/2
#T(N)=((n**2)/2)-(n/2)
#So O(N)=N^2
