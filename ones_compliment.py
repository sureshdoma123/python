#one's compliment of number
def ones_comp(n):
    if n==0:
        return 1
    r=[]
    while n:
        d=n%2
        n=n//2
        r.append(d)
    r.reverse()
    #print(*r)
    for i in range(len(r)):
        if r[i]==1:
            r[i]=0
        else:
            r[i]=1
    #print(*r)
    l=len(r)-1
    i=s=0
    while(l!=-1):
        s+=r[l]*(2**i)
        l-=1
        i+=1
    #print(s)
    return s,r

n=int(input("Enter Decimal number:"))
res=(ones_comp(n))
print("Ones's compliment of Decimal num in decimal num :",res)
