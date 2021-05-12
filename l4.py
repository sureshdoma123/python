#separate the list elements into different lists

def evodlist(data,evl,odl,num):
    for i in range(num):
        if data[i]%2==0:
            evl.append(data[i])
        else:
            odl.append(data[i])

n=int(input())
data=list(map(int,input().split()))
evenlist=[]
oddlist=[]
evodlist(data,evenlist,oddlist,n)
print("Even List is:",evenlist)
print("Odd List is:",oddlist)
oddlist.extend(evenlist)
print()
for i in oddlist:
    print(i,end=',')

'''
o/p:
5
12 13 14 15 16
Even List is:  [12, 14, 16]
Odd List is:  [13, 15]

13,15,12,14,16
'''
