a,b,c = map(int,input().split())
hyp = c*c
adj = a*a
opp = b*b
if(hyp == adj + opp):
  print("yes")
 else:
  print("no")
