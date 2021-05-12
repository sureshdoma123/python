n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        if j==1:
            print("0",end="")
        elif j==i:
            print("1",end="")
            
        else:
            print("0",end="")
            
    print()

"""
0
01
001
0001
00001

"""
