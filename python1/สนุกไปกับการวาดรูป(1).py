print("*** Fun with Drawing ***")
n = int(input("Enter input : "))
dot = n - 1

def pattern(dot, pos):
  print(dot * '.',end='')
  print('*',end='')
  if pos > 0:
    print('+' * pos + '*', end='')
  print((2*dot-1) * '.',end='')
  print('*',end='')
  if pos > 0:
    print('+' * pos + '*', end='')
  print(dot * '.')

cnt = -1
for i in range(dot, 0, -1):
  pattern(i, cnt)
  cnt += 2
print('*' + '+'*(2*n - 3) + '*' + '+'*(2*n-3) + '*')
dot = 1
pos = 4*n-7
while(pos > 0):
  print('.'*dot + '*' + '+' * pos + '*' + '.'*dot)
  pos -= 2
  dot += 1
print('.'*(2*n-2) + '*' + '.'*(2*n-2))
