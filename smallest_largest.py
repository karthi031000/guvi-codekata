N = int(input())
lst = list(map(int,input().split()))
mini = min(lst)
maxi = max(lst)
pos1 = index(mini) + 1
pos2 = index(maxi) + 1
print(pos1,pos2)
