n=int(input())
a=0
b=1
count=0
print(a,b,end=" ")
while n!=count:
    f=a+b
    print(f,end=" ")
    a=b
    b=f
    count+=1

# 2nd MOdel
'''
def fibb(n):
    a=0
    b=1
    i=3
    print(a,b,end=" ")
    while i<=n:
        c=a+b
        if c<=n:
            print(c,end=" ")
            a=b
            b=c
            i+=1
        else:
            break
           

n=int(input())
fibb(n)
'''
