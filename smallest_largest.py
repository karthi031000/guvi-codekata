N = int(input())
lst = list(map(int,input().split()))
a = min(lst)
b = max(lst)
pos1 = lst.index(a) + 1
pos2 = lst.index(b) + 1
print(pos1,pos2)

