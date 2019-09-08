N = int(input())
lst = list(map(int,input().split()))
mini = min(lst)
maxi = max(lst)
pos1 = lst.index(mini) + 1
pos2 = lst.index(maxi) + 1
print(pos1,pos2)
