
n=int(input())
data=list(map(int,input().split()))
l=[]
for i in data:
    l.append(i)
l.sort()
if (l==data) or (data==l[::-1]):
    print("Sorted order")
else:
    print("Not a Sorted order")


