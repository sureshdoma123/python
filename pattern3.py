n=int(input())
for i in range(1,n+1):
    j=i
    for j in range(1,n+1,1):
        print(j,end=" ")
    n-=1
    print()
    
