def check_prime(n): #for checking wheather prime or not
    if n > 1:
        if n == 2: return True
        for i in range(2,n):
            if n % i == 0:
                return False
                break
        return True
    return False
def primeproduct(m): #for checking wheather prime product or not 
    if m >= 0:
      for i in range(1,m):
        if m%i == 0 and check_prime(i) and check_prime(m//i):
            return True
            break
      return False
n=int(input())
print(check_prime(n))
print(primeproduct(n))
