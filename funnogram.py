#Funnogram program

s1=input("Enter String 1: ")
s2=input("Enter String 2: ")
d1={}
d2={}
for i in s1:
    if i not in d1.keys():
        d1[i]=1
    else:
        d1[i]+=1
for i in s2:
    if i not in d2.keys():
        d2[i]=1
    else:
        d2[i]+=1

if(d1==d2):
    print(True)
else:
    print(False)
