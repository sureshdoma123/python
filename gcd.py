n1,n2=map(int,input().split())
while True:
    if n1<n2:
        n1,n2=n2,n1
    else:
        n1=n1%n2
    if n1==0:
        break
print("GCD is :",n2)
