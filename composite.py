n = int(input())
if(n >= 1):
  for i in range(1,n):
    if(n % i == 0):
      print("yes")
   else:
    print("no")
else:
  print("no")
