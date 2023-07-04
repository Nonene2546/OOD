print("*** String Rotation ***")
a, b = [x for x in input("Enter 2 strings : ").split()]
n = len(a)
a1 = a
b1 = b
cnt = 1
a = a[-1] + a[:-1]
b = b[1:] + b[0]
print(cnt, a, b)
while(a1 != a or b1 != b):
  cnt += 1
  a = a[-1] + a[:-1]
  b = b[1:] + b[0]
  if cnt <= 5:
    print(cnt, a, b)

if cnt > 6:
  print(" . . . . . ")

if cnt > 5:
  print(cnt, a, b)

print(f"Total of  {cnt} rounds.")