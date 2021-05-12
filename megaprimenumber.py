num=int(input("Enter a number"))
def isprime(num):
    for i in range(1,num+1):
        if(num%i==0):
            return False
        return True
def count(num):
    c=0
    while num:
        num=num//10
        c+=1
    return c
pc=count(num)
while num:
    mpc=0
    r=num%10
    num=num//10
    while r:
        for i in range(1,r+1):
            if(r%i==0):
                mpc+=1
            else:
                break
    #print(r)
    #mp=isprime(r)
    #if(mp=isprime(r)):
        #mpc+=1

if(mpc==pc):
    print("Megaprime")
else:
    print("Not a mega prime")
