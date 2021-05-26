#To convert binary to decimal
def Bin_to_dec(n):
    k=[]
    while n:
        r=n%10
        n=n//10
        k.append(r)
    k.reverse()
    l=len(k)-1
    x=i=0
    while(l!=-1):
        x+=k[l]*(2**i)
        l-=1
        i+=1
    return x

n=int(input("Enter a number: "))
print("Decimal number is:",Bin_to_dec(n))
