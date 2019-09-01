n = int(input())
ch = map(int,input().split())
lst = ch.split()
ln = 2
for i in range(0,len(lst),ln):
               yield[i:i + ln]
  
  
