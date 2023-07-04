s = input("Enter secret code : ")
unique = set()
for i in s:
  if i in unique:
    print((ord(i) - 96) * 4)
    exit(0)
  else:
    unique.add(i)