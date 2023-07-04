class MyInt:
  def __init__(self, n):
    self.number = n

  def __sub__(self, n):
    return self.number - n.number//2
  
  def isPrime(self):
    if self.isPrimeHelper(self.number):
      return "True"
    return "False"
  
  def isPrimeHelper(self, n):
    if n <= 1:
      return False
    
    if n == 2 or n == 3:
      return True
    
    if n % 2 == 0 or n % 3 == 0:
      return False
     
    for i in range(5, int(n**(0.5))+1, 6):
      if n % i == 0 or n % (i + 2) == 0:
        return False
 
    return True
  
  def showPrime(self):
    if(self.number < 2):
      return "!!!A prime number is a natural number greater than 1"
    ans = ""
    for i in range(2, self.number+1):
      if(self.isPrimeHelper(i)):
        ans += str(i) + ' '
    return ans

print(" *** class MyInt ***")
a, b = [int(x) for x in input("Enter 2 number : ").split()]
a = MyInt(a)
b = MyInt(b)

print(f'{a.number} isPrime : {a.isPrime()}')
print(f'{b.number} isPrime : {b.isPrime()}')
print(f"Prime number between 2 and {a.number} : {a.showPrime()}")
print(f"Prime number between 2 and {b.number} : {b.showPrime()}")
print(f'{a.number} - {b.number} = {a-b}')