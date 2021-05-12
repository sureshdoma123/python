#sum of even and odd fibbnocci upto n
def fibbes(n,n1):
    a=fes=0
    b=1
    i=3
    print(a,b,end=" ")
    while i<=n:
        c=a+b
        if c<=n:
            if c%2==0:
                fes+=c
            if c>n1:
                print(c,end=" ")
            a=b
            b=c
            i+=1
        else:
            break
    return fes
#sum of odd fibbnocci upto n
def fibbos(n):
    a=0
    b=fos=1
    i=3
    while i<=n:
        c=a+b
        if c<=n:
            if c%2==1:
                fos+=c
            a=b
            b=c
            i+=1
        else:
            break
    return fos
#Difference between even sum and odd sum
def diff(a,b):
    if(a>=b):
        c=a-b
    else:
        c=b-a
    return c
#fibbnocci series from n1 to n2 range
def fibbrange(n1,n2):
    a=0
    b=1
    i=3
    ld=0
    while i<=n2:
        c=a+b
        if c<=n2:
            if c>n1:
                print(c,end=" ")
            a=b
            b=c
            ld=c
            i+=1
        else:
            break
    return ld
##n=int(input())
##n1,n2=map(int,input("Enter the rane of numbers: ").split())
##es=fibbes(n,10)
##os=fibbos(n)
##print("\nEven sum of Fibbnocci series:",es)
##print("Odd  sum of Fibbnocci series:",os)
##print("Difference is :",diff(es,os))
##ld=fibbrange(n1,n2)
