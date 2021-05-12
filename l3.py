#count of even and odd numbers in a list

#1st model

def rev(num):
    rn=0
    while num:
        r=num%10
        num=num//10
        rn=rn*10+r
    return rn

def reverselist(data,num):
    for i in range(num):
        data[i]=rev(data[i])

n=int(input())
data=list(map(int,input().split()))
mi1=data.index(max(data))
reverselist(data,n)
mi2=data.index(max(data))

if mi1==mi2:
    print("Perfect")
else:
    print("Not Perfect")

#2nd Model
    
'''
def reverse(num):
    rev=0
    while num:
        r=num%10
        num=num//10
        rev=rev*10+r
    return rev

def reverseList(data,n):
    for i in range(n):
        data[i]=reverse(data[i])

    
def findMaxPos(data,n):
    mi=0
    m=data[0]
    for i in range(1,n):
        if m<data[i]:
            m=data[i]
            mi=i
    return mi
    
n=int(input())
data=list(map(int,input().split()))
m1=findMaxPos(data,n)
reverseList(data,n)
m2=findMaxPos(data,n)
if m1==m2:
    print("perfect")
else:
    print("not perfect")
'''
