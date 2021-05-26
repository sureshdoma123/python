##n=int(input())
##l=[]
##for i in range(1,n+1):
##    l.append(i)
###print(*l)
##for i in range(len(l)):
##    for j in range(i+1):
##        if l[j]==

##n=int(input())
##k=1
##for i in range(1,n+1):
##    for j in range(1,i):
##        print(k,end=" ")
##        k+=1
##    if k==5:
##        break
##    print()
n=int(input())
k=1
c=0
for i in range(1,n):
      for j in range(1,i):
            print(k,end=" ")
            k=k+1
            if k>n:
                  break
      if k>n:
            break
      print()
print()
print("Noof completed rows is: ",c)
'''
n=10

1
2 3
4 5 6
7 8 9 10
'''
