a,b,c = map(int,input().split())
if(a + b > c):
  if(a + c > b):
    if(b + c > a):
      print("yes")
     else:
      print("no")
    else:
      print("no")
  else:
    print("no")
else:
  print("no")
