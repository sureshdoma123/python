num=int(input("Enter a number:"))
ac=0
dc=0
tc=0
while num:
    d=num%10
    num=num//10
    e=num%10
    if(d>e):
        d,e=e,d
        ac+=1
    else:
        dc+=1
    tc+=1
if(ac==tc):
    print("All digits are in Ascending order")
elif(dc==tc):
    print("All digits are in Descending order..")
else:
    print("The digits are not following order..")

        
        
        
