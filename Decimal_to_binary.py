#To convert Decimal to binary
n=int(input("Enter a number: "))
def Dec_to_bin(n):
    res=[]
    while n:
        r=n%2
        n=n//2
        res.append(r)
    res.reverse()
    return res

l=Dec_to_bin(n) #result is in list format
print("Binary of given number is:",*l)
