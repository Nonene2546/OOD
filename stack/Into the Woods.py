class Stack:
  def __init__(self):
    self.items = []
  
  def push(self, i):
    self.items.append(i)
  
  def pop(self):
    value = self.items[-1]
    self.items.pop()
    return value

  def top(self):
    return self.items[-1]
  
  def isEmpty(self):
    return len(self.items) == 0
  
  def size(self):
    return len(self.items)
  
st = Stack()
  
s = input('Enter Input : ').split(',')
for i in s:
  if i[0] == 'A':
    st.push(int(i[2:]))
  else:
    tmp = Stack()
    if not st.isEmpty():
      mx = st.pop()
      tmp.push(mx)
      cnt = 1
    else:
      cnt = 0
    while(not st.isEmpty()):
      value = st.pop()
      tmp.push(value)
      if mx < value:
        mx = value
        cnt += 1
    print(cnt)
    while(not tmp.isEmpty()):
      st.push(tmp.pop())