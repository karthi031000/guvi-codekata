n = int(input())
#if(n == 1):
# print("no")
for i in range(2,n):
  if(n % i != 0):
    print("no")
  else:
    print("yes")
    break
