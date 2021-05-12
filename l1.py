n=int(input())
data=list(map(int,input().split()))
ec=0
oc=0
#index based looping
for i in range(n):
    if (data[i]%2==0):
        ec+=1
    else:
        oc+=1
print("even count=",ec)
print("Odd count=",oc)



#Value based looping
##for i in data:
##    print(i,end=' ')

##data=[]
##for i in range(n):
##    k=int(input())
##    data.append(k)
