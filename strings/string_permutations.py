#converts list to string
def listToString(a):
  return ''.join(a)

#finds permutatons
def permute(a, l, r):
  if l==r:
    print(listToString(a))
  else:
    for i in range(l,r+1):
      a[l], a[i] = a[i], a[l]
      permute(a, l+1, r)
      # go back to previous index--- backtracking
      a[l], a[i] = a[i], a[l] 
 
string = "ABC"
n = len(string)

# convert string to list
a = list(string)
permute(a, 0, n-1)
