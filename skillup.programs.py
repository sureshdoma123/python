#print a Table Format
'''a=int(input("enter a num:"))
b=int(input("enter a num:"))
n=int(input("enter a Table number:"))
for i in range(a,b,-1):
    print(i,"*",n,"=",n*i)'''

#Check Prime Number or Not
'''n=int(input("enter a num:"))
count=0
for i in range(1,n+1):
  if n%i==0:
        count+=1
if count==2:
    print(n,'is prime num')
else:
    print(n,'is not a prime num')'''

#Print a Table Form
'''a=int(input("enter range:"))
b=int(input("enter a range"))
n=int(input("enter a table number:"))
if a<=b:
    i=a
    while i<=b:
        print(n,'*',i,'=',n*i)
        i+=1
else:
    i=a
    while i>=b:
        print(n,'*',i,'=',n*i)
        i-=1'''


#Amstrong Number    
'''num=int(input("enter number:"))
sum=0
a=num
while num>0:
    rem=num%10
    sum+=(rem*rem*rem)
    num=num//10
if a==sum:
    print(a,'is amstrong number')
else :
    print(a,'is not an amstrong number')'''

#Reverse of a Number
'''num=int(input("enter a number:"))
rev=0
while num>0:
    rem=num%10
    rev=rev*10+rem
    num=num//10
print(rev)'''

#Reverse Order Using Strings
'''num=input("enter a number:")
print(num[::-1])'''


#Check Palindrome Number or Not
'''num=int(input("enter a number:"))
rev=0
a=num
while num>0:
    rem=num%10
    rev=rev*10+rem
    num=num//10
if a==rev:
    print(a,'is Palindrome Number')
else :
    print(a,'is Not a Palindrome Number')'''

 
#Prime Num or Not Using While loop
'''n=int(input("enter a number:"))
count=0
i=1
while i<=n:
    if n%i==0:
        count+=1
    i+=1
if count==2:
    print(n,'is Prime Number')
else:
    print(n,'is Not a Prime Number')'''

#Print '*' Pattern
'''n=int(input('enter a num:'))
for i in range (1,n+1):
    for j in range(1,n+1):
        print('*',end=' ')
    print()'''

'''n=int(input('enter a num:'))
for i in range (1,n+1):
    for j in range(1,i+1):
        print('*',end=' ')
    print()'''

#Reverse '*' Pyramid 
'''n=int(input('enter a num:'))
for j in range (1,n+1):
    for i in range(j,n+1):
        print('*',end=' ')
    print()'''

#'*' pattern
'''rows=int(input('enter num'))
for i in range(1,rows+1):
    for j in range(rows,0,-1):
        if j>i:
            print(" ",end=' ')
        else:
            print('*',end=' ')
    print("")'''

#Print '*' pattern
'''rows=int(input('enter num'))
for i in range(1,rows+1):
    for j in range(rows,0,-1):
        if j>i:
            print(" ",end=' ')
        else:
            print(' * ',end=' ')
    print("")'''

'''n=int(input('enter a num:'))
for i in range (1,n+1):
    for k in range(n,i,-1):
        print(' ',end='')
    for j in range(1,n+1):
        print('*',end='')
    print()'''

#seperate the elements in a List
'''a=[45.343,34,'sachin',12,-36.98,'kohli']
i=[]
f=[]
s=[]
for j in a:
    if type(j)==int:
        i.append(j)
    elif type(j)==float:
        f.append(j)
    else:
        s.append(j)
print('int',i)
print('float',f)
print('string',s)'''

#To check the list elemets have prime numbers or not
'''def prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
        else:
            return True
a=list(map(int,input('enter list elements:').split()))
for i in a:
    if prime(i)==True:
        print(i)'''
#print elements in list by using Index position
'''a=[1,3,2,56,3,2,5,4]
se=0
so=0
for i in range(len(a)):
    if i%2==0:
        se+=a[i]
    else:
        so+=a[i]
print(se)
print(so)'''

#a=open('sample123.txt','x')

a=open(r'C:\Users\hp\Desktop\Filehandling\sample123.txt','r+')
a.write("\n")
a.close()
