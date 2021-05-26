n1,n2=map(int,input().split())
res,r=1,2
while True:
    if n1%r==0 and n2%r==0:
        n1=n1//r
        n2=n2//r
        res=res*r
    else:
        r+=1
    if n1<r or n2<r:
        break
print("LCM is :",res*n1*n2)
