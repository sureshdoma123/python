# Check whether the entered num iz happy number or not

def HappyNumber(num):#19
    rem=sum=0;
    while(num>0):#19>0,1>0
        rem=num%10;#9,1
        sum=sum+(rem*rem);#81,82
        num=num//10;#1,0
    return sum;#82
num=int(input("Enter a number:"))   
result=num;    
while(result!=1 and result!=4):
    result=HappyNumber(result)
if(result==1):
    print("Happy Number:",num)       
elif(result==4):
    print("Not a Happy number:",num)
