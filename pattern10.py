n=int(input())
k=n
for i in range(1,n+1):#row loop
    for j in range(1,k):#space loop
        print(" ",end="")
    k-=1
    for s in range(1,i+1):#col loop
        print("*",end="")
    print()
    
"""
    *
   **
  ***
 ****
*****
"""
