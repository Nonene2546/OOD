s = input('Enter expresion : ')

op = ['[', '(', '{']
cl = [']', ')', '}']

st = []

for i in s:
  if i in op:
    st.append(i)
  elif len(st) > 0 and i in cl:
    if st[-1] == op[cl.index(i)]:
      st.pop()
    else:
      print(f'{s} Unmatch open-close')
      exit(0)
  elif i in cl:
    print(f'{s} close paren excess')
    exit(0)

if len(st) > 0:
  print(f'{s} open paren excess   {len(st)} : ', end='')
  for i in st:
    print(i, end='')
else:
  print(f'{s} MATCH')