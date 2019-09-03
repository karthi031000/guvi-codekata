n,m = map(int,input().split())
sum = n + m
res = sum % 2
if(res == 0):
  print("even")
else:
  print("odd")
