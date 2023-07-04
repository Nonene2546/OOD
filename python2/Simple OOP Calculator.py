class Calculator :
  def __init__(self, n):
    self.number = n

  def __add__(self, n):
    return self.number + n.number

  def __sub__(self, n):
    return self.number - n.number
  
  def __mul__(self, n):
    return self.number * n.number

  def __truediv__(self, n):
    return self.number / n.number

x,y = input("Enter num1 num2 : ").split(",")

x,y = Calculator(int(x)),Calculator(int(y))

print(x+y,x-y,x*y,x/y,sep = "\n")