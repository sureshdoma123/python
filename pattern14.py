n=int(input())
k=n-1
for i in range(1,n+1):
    for s in range(k):
        print(" ",end="")
    k-=1
    for j in range(1,i*2):
        if(i%2==0 and j==1) or (i%2==0 and j==(i*2)-1):
            print("+",end="")
        else:
            print("*",end="")
    print()

'''
    *
   +*+
  *****
 +*****+
*********
'''
