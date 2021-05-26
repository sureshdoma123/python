##def DecimalToBinary(num):
##    if num >= 1:
##        DecimalToBinary(num // 2)
##        if num%2==1:
##            print('0',end="")
##        else:
##            print('1',end="")
##    
##
##def binaryToDecimal(binary):
##      
##    binary1 = binary
##    decimal, i, n = 0, 0, 0
##    while(binary != 0):
##        dec = binary % 10
##        decimal = decimal + dec * pow(2, i)
##        binary = binary//10
##        i += 1
##    print(decimal)
##    
##n=int(input())
##b=int(input())
##DecimalToBinary(n)
##print()
##binaryToDecimal(b)

n=int(input())
data=[]
d=0
while(n):#10 5 2 1
      d=n%2
      n=n//2
      data.append(d)#0 1 0 1#5 2 1
data.reverse()
print(*data)
