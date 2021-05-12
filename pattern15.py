n=int(input())
k=n-1
for i in range(1,n+1):
    for s in range(1,k+1):
        print(" ",end="")
    k-=1
    for j in range(1,i*2):
        if (i%2==0 and j==i):
            print("+",end="")
        else:
            print("*",end="")
    print()
    
'''
    *
   *+*
  *****
 ***+***
*********
'''
