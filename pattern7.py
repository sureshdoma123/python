n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        if j%2==0:
            print("1",end="")
        else:
            print("0",end="")
    print()
    

'''
0
01
010
0101
01010
'''
