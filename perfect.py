import math
n,m = map(int,input().split())
prod = n * m
sqr = math.sqrt(prod)
res = prod * prod
if(res == prod):
  print("yes")
 else:
  print("no")
