#Leetcode Arranging coins program...
#with time complexity
'''
n=int(input())
k=1
c=0
for i in range(1,n):
      for j in range(1,i):
            if j==i-1:
                  c+=1
            print(k,end=" ")
            k=k+1
            if k>n:
                  break
      if k>n:
            break
      print()
print("\n",c)
'''
#without Time complexity
n=int(input())
k,c=1,0
while n>=k:
      print(k,end=" ")
      n=n-k
      c+=1
      k+=1
print("\n",c)
'''
n=10

1
2 3
4 5 6
7 8 9 10
'''
