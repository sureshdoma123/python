def totalmoneybank(num):
    m=0
    dm=0
    for i in range(1,num+1):
        if i%7==1:
            m=m+1+dm
        if i%7==2:
            m=m+2+dm
        if i%7==3:
            m=m+3+dm
        if i%7==4:
            m=m+4+dm
        if i%7==5:
            m=m+5+dm
        if i%7==6:
            m=m+6+dm
        if i%7==0:
            m=m+7+dm
            dm+=1
    return m
n=int(input())
print(totalmoneybank(n))
            
