##n=int(input())
##k=n-1
##for i in range(0,n):
##    for j in range(0,k):
##        print(end=" ")
##    k-=1
##    for j in range(0,i+1):
##        print("* ",end="")
##    print()

'''
    * 
   * * 
  * * * 
 * * * * 
* * * * *
'''

#2nd model

n=int(input())
k=n-1  
for i in range(1,n+1):
    for s in range(k):
        print(" ",end="")
    k-=1
    for j in range(1,i*2):
        print("*",end="")
    print()


'''
     *
    ***
   *****
  *******
 *********
'''
