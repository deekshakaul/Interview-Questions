#There are n houses build in a line, each of which contains some value in it. 
#A thief is going to steal the maximal value of these houses, but he can’t steal in two adjacent houses because 
#owner of the stolen houses will tell his two neighbour left and right side. What is the maximum stolen value.


#a-money that can be stolen from houses. n- number of houses
a=list(map(int,input().strip().split(' ')))
n=len(a)
if n == 0:
    print(0)
elif n == 1:
    print(a[0])
elif n == 2:
    print(max(a[0], a[1]))
else:
  M = [0]*n
  M[0] = a[0]
  M[1] = max(a[0], a[1])
# value at i + money till i-2 or money till i-1 since two neighbours cannot be robbed
  for i in range(2, n):
      M[i] = max(a[i]+M[i-2], M[i-1])
  print(M[-1])      
