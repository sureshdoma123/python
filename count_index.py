n=int(input())
data=list(map(int,input().split()))
c=0
for i in range(n-1):
    if(data[i]==1 and data[i+1]==1 and data[i+2]==1):
        c+=i
print(c)
