n,k = map(int,input().split())
lst = list(map(int,input().split()))
for i in range(0,len(lst)):
  if(lst[i] == k):
    print("yes")
  else:
    print("no")
