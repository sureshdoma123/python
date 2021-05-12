n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        if(i%2==0 and j%2==0) or (i%2==1 and j%2==1):
            print(j,end=" ")
        else:
            print(j,end=" ")
            
    print()
    

'''
1
21
123
4321
12345
'''
