def rev(n):
    rev=0
    while n:
        r=n%10
        n=n//10
        rev=rev*10+r
    return rev
    



n1=int(input("n1:"))
n2=int(input("n2:"))
s=0
l={1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
if(n1<=9):
    for i in range(n1,n2+1):
        if(i>9):
            break
        else:
            print(l[i])
            s=s*10+i
s=rev(s)
while s:
    r=s%10
    s=s//10
    if(r%2==0):
        print("even")
    else:
        print("odd")
            
                
