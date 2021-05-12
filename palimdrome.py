##Palindrome number or not

num=int(input("Enter a number:"))
rev=0
pn=num
while num:
    r=num%10
    num=num//10
    rev=rev*10+r
    
if pn==rev:
    print(pn,"is a Palindrome number")
else:
    print(pn,"is Not a palindrome number")

