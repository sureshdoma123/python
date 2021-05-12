## print the following cases
##I.Number Consists of all even num then print Even numbers
##II.all odd numbers then print odd number
##III.mix of both even and odd print mixed numbers

num=int(input())
ce=0
co=0
es=0
os=0
tc=0
while num:
    d=num%10
    num=num//10
    if(d%2==0):
        ce+=1
        es+=d
    else:
        co+=1
        os+=d
    tc+=1
if(ce==tc):
    print("All Digits are Even Numbers and Sum is:",es)
elif(co==tc):
    print("All digits are Odd Numbers an sum is:",os)
else:
    print("All digits are Mixed Numbers of Even & Odd and sum is:",es+os)
