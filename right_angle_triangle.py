a,b,c = map(int,input().split())
hyp = c*c
adj = a*a
opp = b*b
res = opp + adj
if(hyp == res):
  print("yes")
 else:
  print("no")
