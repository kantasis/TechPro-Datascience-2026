def isPrime(n):
   for i in range(2,n):
      print(f"Checking {i}")
      if n%i == 0:
         return False
   return True

print(isPrime(1))
