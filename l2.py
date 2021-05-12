'''
def findevenpos(data,n):
    for i in range(n):
        if data[i]%2==0:
            break
    return i
n=int(input())
data=list(map(int,input().split()))    
print(findevenpos(data,n))
'''

'''
def findevenpos(data,n):
    for i in range(n):
        if data[i]%2==0:
            return i
n=int(input())
data=list(map(int,input().split()))    
k=findevenpos(data,n)
print(k,data[k])
'''

def rev(num):
    rn=0
    while num:
        r=num%10
        num=num//10
        rn=rn*10+r
    return rn

def revlist(data,num):
    for i in range(num):
        data[i]=rev(data[i])

n=int(input())
data=list(map(int,input().split()))
revlist(data,n)
for i in data:
    print(i,end=' ')

        
