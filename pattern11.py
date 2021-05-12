n=int(input())
k=1
for i in range(n,0,-1):
    for s in range(1,k):
        print(" ",end="")
    k+=1
    for j in range(1,i+1):
        print("*",end="")
    print()

#2nd model
'''    
for i in range(1,n+1):
    for j in range(1,n+1):
        if(j<i):
            print(" ",end="")
        else:
            print("*",end="")

    print()
'''

"""
*****
 ****
  ***
   **
    *
"""
