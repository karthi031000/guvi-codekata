n = int(input())
if(n >= 1):
  for i in range(1,n):
    if(n % i == 0):
      print("no")
   else:
    print("yes")
else:
  print("no")
