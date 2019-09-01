lst1 = []
def swap(lst,n):
    for i in range(0,n,2):
        temp = lst[i]
        lst[i] = lst[i+1]
        lst[i+1] = temp
        a = lst[i]
        b = lst[i+1]
        c = lst1.extend([a,b])
    return lst1
n = int(input())
lst = list(map(int,input().split()))
if (n%2 != 0):
    swap(lst,n-1)
    d = lst[-1]
    lst1.append(d)
else:
    swap(lst,n)
s = [str(i) for i in lst1]
res = "".join(s)
print(res)
