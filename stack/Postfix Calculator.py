class Stack:
  def __init__(self, ls = None):
    if ls:
      self.ls = ls
    else:
      self.ls = []

  def push(self,i):
    self.ls.append(i)

  def pop(self):
    value = self.ls[-1]
    self.ls.pop()
    return value
  
  def isEmpty(self):
    return len(self.ls) == 0
  
  def size(self):
    return len(self.ls)
  
op = ['+', '-', '*', '/']
    
def postFixeval(st):

  s = Stack()

  for i in st:
    if i in op:
      a = s.pop()
      b = s.pop()
      if i == '+':
        s.push(a+b)
      elif i == '-':
        s.push(b-a)
      elif i == '*':
        s.push(a*b)
      else:
        s.push(b/a)
    else:
      s.push(int(i))

  return s.pop()

            


print(" ***Postfix expression calcuation***")

token = list(input("Enter Postfix expression : ").split())



print("Answer : ",'{:.2f}'.format(postFixeval(token)))