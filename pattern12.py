n=int(input())
k=1
for i in range(1,n+1):
    for s in range(1,k):
        print(" ",end="")
    k+=1
    for j in range(n,i-1,-1):
        print(j,end="")
    print()


"""
54321
 5432
  543
   54
    5
"""
