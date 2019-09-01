n = int(input())
lst = list(map(int,input().split()))
lst1 = []
for i in range(0,n,2):
    temp = lst[i]
    lst[i] = lst[i+1]
    lst[i+1] = temp
    a = lst[i]
    b = lst[i+1]
    lst1.extend([a,b])
    if(i % 2 == 0 and n % 2 != 0):
        lst1.append(lst[-1])
        break
print(lst1)
