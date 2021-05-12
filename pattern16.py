n=int(input())
k=0
for i in range(n+1,0,-1):
    for s in range(k):
        print(" ",end="")
    k+=1
    for j in range(1,i*2):
        print("*",end="")
    print()

'''
***********
 *********
  *******
   *****
    ***
     *
'''
