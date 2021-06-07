##a=int(input('enter a number : '))
##if a%2==0:#first
##    print(a,' is even')
##    if a<10:#second
##        print(a,'is less than 10')
##    else:#second
##        print(a,' is greater than 10')
##else:#first
##    print(a,' is odd')
##    if a<10:#second
##        print(a,'is less than 10')
##    else:#second
##        print(a,' is greater than 10')
    

##a=int(input('enter a number: '))
##b=int(input('enter a number'))
##print(a,b)
##
##a,b,c,d=map(int,input().split())
##print(a+b+c+d)
##
##a,b=map(int,input('enter a number to check which is greater').split())
##if a>b:
##    print(a,'is greater 1')
##else:
##    if a==b:
##        print("both are same")
##    else:
##        print(b,'is greater 2')
##
##
##if a>=b:
##    if a==b:
##        print("both are same")
##    else:
##        print(a,'is greater 1')
##else:
##    print(b,'is greater 2')


##m=int(input('enter marks'))#51
##if m>=80:#51>=80
##    print('A grade')
##elif m>=60 and m<80:#51>=60(false) and 51<80(true)
##    print('B grade')
##elif m>=40 and m<60:#51>=40(true) and 51<60(true)
##    print('C grade')
##else:
##    print('Failed')

##did='python@thub.com'
##dpwd='python123'
##
##uid=input("enter a mail id")
##upwd=input("enter a password")
##
##if did==uid and dpwd==upwd:
##    print('login successfully')
##else:
##    print('wrong credentials')


##a=10
##b=20
##
##temp=a#10
##a=b#20
##b=temp#10
##a=a+b#10+20=30
##b=a-b#30-20=10
##a=a-b#30-10=20
##a,b=b,a
##print('a=',a)
##print('b=',b)


##if year%4==0:
##    if year%100==0:
##        if year%400==0:
##            print('true')
##        else:
##            print('false')
##    else:
##        print('true')
##else:
##    print('false')


##year=int(input('enter a leap year: '))
##if year%4==0 and year%100!=0 or year%400==0:
##    print('true')
##else:
##    print("false")
##
##def add():
##    a=10
##    b=2000
##    return(a+b)
##
##print(add())


##def add(a,b):#formal parameters
##    return(a+b)
##n=int(input('enter a number'))#23
##m=int(input('enter a number'))#34
##print(add(n,m))#actual parameters

##a=10#global variable
##print(a,'1')#10
##
##def ex():
##    global i
##    i=11#local variable
##    i+=1
##    print(i,'2')#12
##
##ex()
##
##print(i,'3')#10


##def ex(n,m,c=23):
##    return(n+m+c)
##a=int(input())
##b=int(input())
##print(ex(a,b))


##def add(a,b):
##    return(a+b)
##def sub(a,b):
##    return(a-b)
##def mul(a,b):
##    return(a*b)
##def div(a,b):
##    return(a%b)
##
##a=int(input())
##b=int(input())
##ch=int(input('enter ur choice 1: add 2:sub , 3:mul,4:div'))
##if ch==1:
##    print(add(a,b))
##elif ch==2:
##    print(sub(a,b))
##elif ch==3:
##    print(mul(a,b))
##elif ch==4:
##    print(div(a,b))
##else:
##    print('wrong choice')

###from math import floor
##import math
##
##a=math.floor(-43.35687)
##print(a)
##
##a=ceil(-23.2432443)
##print(a)


##def ex(a,b):
##    a+=1
##    b+=2
##    return(a+b)
##a=int(input("enter a number:"))#10
##b=int(input("enter a number:"))#11
##print(ex(a,b))


##a=int(input("enter a range"))
##b=int(input("enter a range"))
##n=int(input("enter a number"))
##if a<=b:
##    for i in range(a,b+1,1):#5  10
##        print(n,"*",i,"=",i*n)
##else:
##    for i in range(a,b-1,-1):#10 5
##        print(n,"*",i,"=",i*n)    

##n=int(input('enter a number'))#4
##cnt=0
##for i in range(1,n+1):#(1,5) 1,2,3,4
##    if n%i==0:#4%1==0,4%2==0,4%4==0
##        cnt+=1#1,2,3
##
##if cnt==2:#3==2
##    print(n,' is prime number')
##else:
##    print(n,' is not a prime')

##n=int(input('enter a number'))#4
##for i in range(2,n):#(2,4)  2
##    if n%i==0:##4%2==0
##        print(n,' is not a prime')
##        break
##else:
##    print(n,' is prime number')
##


##
##for i in range(1,6):
##    print(i)
##    if i==3:
##        break
##else:
##    print('loop done')
##print('terminate')

##a=int(input("enter a range"))#15
##b=int(input("enter a range"))#5
##n=int(input("enter a number"))
##if a<=b:
##    i=a
##    while i<=b:
##        print(i,'*',n,'=',n*i)
##        i+=1
##else:
##    i=a
##    while i>=b:
##        print(i,'*',n,'=',n*i)
##        i-=1    
        
    

##i=1
##while i<11:
##    print(i,'*',2,'=',2*i)
##    if i==5:
##        break
##    i+=1
##
##print("example")

##i=0
##while i<11:#0,1,2,3,4
##    i+=1
##    if i==5:
##        continue
##    print(i,'*',2,'=',2*i)
##
##print("example")

##n=int(input('enter a number'))#234
##s=0
##a=str(n)
##import math
##while n>0:#234,23,2
##    r=n%10#4,3,2
##    s+=int((math.pow(r,len(a))))#s=64+27=91+8=99
##    n=n//10#23,2
##if int(a)==s:
##    print(a,' is armstrong number')
##else:
##    print(a,' is not armstrong number')

##
##n=int(input('enter a number'))#234
##rev=0
##a=n
##while n>0:#234,23,2
##    r=n%10#4,3,2
##    rev=rev*10+r#43*10+2=430+2=432
##    n=n//10#23,2
##if a==rev:
##    print(a,' is a palindrome')
##else:
##    print(a,' is not a palindrome')
##
##
##n=input('enter a number')
##rev=n[::-1]
##if a==rev:
##    print(a,' is a palindrome')
##else:
##    print(a,' is not a palindrome')

##n=int(input('enter a number'))
##for i in range(1,n+1):
##    for j in range(1,n+1):
##        print(i,end="")
##    print()

##n=int(input('enter a number'))
##for i in range(1,n+1):
##    for j in range(1,n+1):
##        print(i,end="")
##    print()

##n=int(input('enter a number'))#5
##for i in range(1,n+1):#(1,2,3,4,5)  1
##    for j in range(n,i-1,-1):#{1:(5,4,3,2,1),2:(5,4,3,2),3:(5,4,3)
##        print(j,end=" ")      #,4:(5,4),5:(5)}
##    print()
    

##n=int(input('enter a number'))#5
##for i in range(1,n+1):#(1,2,3,4,5)  1
##    for j in range(i,n+1):#{1:(1,2,3,4,5),2:(2,3,4,5),3:(3,4,5)
##        print('*',end="")      #,4:(4,5),5:(5)}
##    print()


##for i in range(1,6):
##    for j in range(1,6):
##        print(chr(j+64),end="")
##    print()

##n=int(input("enter a number"))
##for i in range(1,n+1):#rows  1 2
##    for j in range(n-i,0,-1):#empty space {1:(5,4,3,2),2:(5,4,3)}
##        print(" ",end="")
##    for k in range(0,i):#stars  {1:(0),1:(0,1)}
##        print('* ',end="")
##    print()

##n=int(input())
##for i in range(1,n+1):
##    for k in range(n,i,-1):
##        print(' ',end='')
##    for j in range(1,n+1):
##        print('*',end='')
##    print()


##
##n=list(map(int,input().split()))
##print(n,len(n))



##a=[5,3,5,2,8,4,0]
##for i in range(len(a)):#0,1
##    print(i,a[i])#(0,5),(1,3),(2,5),(3,2),(4,8),(5,4),(6,0)
##i=0
##while i<len(a):
##    print(i,a[i])
##    i+=1


##a=[3,5,2,6,3]
##cnt=0
##for i in a:
##    cnt+=1
##    print(i)
##print('element',cnt)

##a=input('enter a string')
##n=input('enter a element')
##cnt=0
##for i in a:
##    if i==n:
##        cnt+=1
##print(cnt)

##a='sachin1313'
##s=0
##for i in a:#sachin13
##    if i in '1234567890':#13
##        s+=int(i)#1+3+1+3
##print(s)
        
##a='sachin1313'
##s=0
##for i in a:#sachin13
##    if i.isdigit():
##        s+=int(i)
##print(s)


#a=list(map(int,input().split()))#[32,43,12,65,34,22]
##print(max(a))
##a.sort()
##print(a[-1])

##m=0#32
##for i in a:#32,43,12,65,34
##    if i>m:#43,65
##        m=i#43,65
##print(m)


##a=['sachin','dhoni','kohli','harbajan']
##l=[]
##for i in a:
##    l.append(len(i))
##print(a)
##print(l)#[6,5,5,6]
##for i in a:#sachin,dhoni,kohli,sehwag
##    if len(i)==max(l):#6==6,6==6
##        print(i)


##a=['S','a','c','H','i','N']
##s=[]
##c=[]
##for i in a:#'S'
##    if ord(i)>=65 and ord(i)<=90:
##        s.append(i)
##    else:
##        c.append(i)
##print(s,c)

##a=[45.234,67,'sachin',89,-98.956,'kohli']
##i=[]
##f=[]
##s=[]
##for j in a:#45.234,67,'sachin'
##    if type(j)==int:
##        i.append(j)
##    elif type(j)==float:
##        f.append(j)
##    else:
##        s.append(j)
##print('int',sum(i))
##print('float',sum(f))
###print('string',s)

##a=[1,4,5,2,6,2,5,3,7]
##b=int(input('enter a element'))
##if b in a:
##    for i in range(len(a)):
##        if a[i]==b:
##            print(i)
##else:
##    print(b,' is not in',a)

##a=[[23,43,65],[21,42,67,65,44],[29,39,76,45]]
##for i in a:#[23,43,65],[21,42,67],[29,39,76]]
##    print(len(i))


##a=[3,6,9,7,13,2]
##sumo=0
##sume=0
##for i in range(0,len(a),2):
##    sumo=sumo+a[i]
##for j in range(1,len(a),2):
##    sume=sume+a[j]
##print(sumo)
##print(sume)


##def prime(n):
##    for i in range(2,n):
##        if n%i==0:
##            return False
##    else:
##        return True
##
##a=[37,60,74,93,5,71]
##for i in a:#3,6,7,9,5,71
##    if prime(i)==True:
##        print(i)

##a=[33,45,12,35,67,89]
##sume=0
##sumo=0
##for i in a:
##    if i%2==0:
##        sume+=i
##    else:
##        sumo+=i
##print(sume,sumo)

##did='python@thub.com'
##dpwd='python123'
##for i in range(4):
##    uid=input("enter a mail id")
##    upwd=input("enter a password")
##
##    if did==uid and dpwd==upwd:
##        print('login successfully')
##        break
##    else:
##        print('wrong credentials')
##else:
##    print('account blocked for 24 hours')

##a=[2,4,6,3]
##b=[5,6]
##for i in b:#5,6
##    if i not in a:#true
##        a.append(i)
##        print(i)
##print(a)

#a=[5,6,7,8,9,10,11,12,13,14,15]

##a={i:i*i for i in range(5,16)}
##print(a)


##a={}
##S1=list(map(int,input().split()))
##S2=list(map(int,input().split()))
##a['s1']=S1
##a['s2']=S2
##print(a)

##a={}
##z=int(input('enter no of students'))
##for i in range(1,z+1):
##    n=input('enter a student name')
##    l=[]
##    m=int(input('enter no of subjects'))
##    for j in range(1,m+1):
##        k=int(input('enter marks'))
##        l.append(k)
##    a[n]=l
##print(a)


##a=open(r'C:\Users\Rajesh\Desktop\filehandling\sample.txt','w')
##a.write("python class\n")
##a.write("file handling\t")
##a.write('how are you')
##a.close()


##a=open(r'C:\Users\Rajesh\Desktop\filehandling\sample.txt','a')
##a.write("python class")
##a.close()

##a=open(r'C:\Users\Rajesh\Desktop\filehandling\sample.txt','r+')
##a.write('good morning\n')
##a.write('python class')
##a.close()

##a=open(r'C:\Users\Rajesh\Desktop\filehandling\sample.txt','r+')
##s=a.readlines()
##for i in s:#1line
##    w=i.split()
##    print(w)

##a=open(r'C:\Users\Rajesh\Desktop\filehandling\sample.txt','r+')
##
##with open(r'C:\Users\Rajesh\Desktop\filehandling\sample.txt','r+') as a:
##    s=a.read()
##    print(s)
##

##import os
##os.remove()
##
##l=[]
##a=open(r'C:\Users\Rajesh\Desktop\filehandling\cars.csv','r+')
##s=a.readlines()
##for i in s:
##    w=i.split()
##    s=w[-1].split(',')
##    l.append(s[2])

##try:
##    a=10
##    open('sample.py')
##    print(a/0)
##    print(a+b)
##except NameError:
##    print('avoid B')
##    print(a)
##except ZeroDivisionError:
##    print('cannot divide by 0')
##    print(a)
##except FileNotFoundError:
##    print('select proper file')
##else:
##    print('no error')
##finally:
##    print("must be executed")


##def prime(n):#2,3,
##    for i in range(2,n):
##        if n%i==0:
##            return False
##            break
##    else:
##        return True
##   
##def semiprime(n):
##    for i in range(2,n):#2,3,4,5
##        if n%i==0:#6%2,6%3,6%4,6%5
##            if prime(i)==False:
##                return (False)
##    else:
##        return(True)
##n=int(input('enter a number : '))
##print(semiprime(n))



##def prime(n):#2,3,
##    for i in range(2,n):
##        if n%i==0:
##            return False
##            break
##    else:
##        return True
##def superprime(n):#5
##    if prime(n)==True:#5
##        cnt=0
##        for i in range(2,n+1):#2,3,4,5
##            if prime(i)==True:
##                cnt+=1#1,2,3
##        if prime(cnt)==True:
##            return True
##        else:
##            return False
##    else:
##        return False
##n=int(input('enter a number : '))
##print(superprime(n))
        
##n=int(input("Enter a Number:"))
##fact=1
##if n<0:
##    print(1)
##else:
##    for i in range(1,n+1):
##        fact=fact*i
##print("Factorial of given umber is :",fact)



##n=int(input("Enter a Number:"))
##def fact(n):
##    fact=1
##    if n==0:
##        return(0)
##    elif n>0:
##        for i in range(1,n+1):
##            fact*=i
##        return(fact)
##    else:
##        print("No factorial of Given Number")
##print("Factorial of given number:",fact(n))

##
##n=int(input("Enter a Number:"))
##def rfact(n):
##    fact=1
##    if n==0:
##        return 1
##    else:
##        return(n*rfact(n-1))
##
##print("Factorial of given number Using Recursive Functions :",rfact(n))


##n=int(input("Enter a Number:"))
##def megaprime(n):
##    if prime(n)==True:
##        while n>0:
##            r=n%10
##            n=n//10
##            if prime(r)==True:
##                cnt=True
##            else:
##                cnt=False
##                return False
##        return cnt
##    else:
##        return False
##
##print(megaprime(n))






































































    







    


