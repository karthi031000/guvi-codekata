n = int(input())
if(n == 1):
  print("no")
for i in range(2,n//2):
  if(n % i != 0):
    print("no")
    break
  else:
    print("yes")
    break
