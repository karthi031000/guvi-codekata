a,b,c = map(int,input().split())
hyp = c*c
adj = a*a
opp = b*b
res = hyp + adj
if(hyp == res):
  print("yes")
 else:
  print("no")
