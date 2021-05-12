'''
n=int(input())
data=list(map(int,input().split()))
f=[]
for i in range(n):
    if data[i] in f:
        pass
    else:
        f.append(data[i])
for i in f:
    print(i,end=' ')
'''

'''
n=int(input())
data=list(map(int,input().split()))
f=[]
for i in data:
    if data.count(i)==1:
        f.append(i)
print(*f)
'''
