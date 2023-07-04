a = [int(x) for x in input("Enter Your List : ").split()]

if(len(a) < 3):
  print("Array Input Length Must More Than 2")
  exit(0)

ans = []

for i in range(len(a)):
  for j in range(i+1, len(a)):
    for k in range(j+1, len(a)):
      if(a[i] + a[j] + a[k] == 5):
        tmp = list(sorted([a[i], a[j], a[k]]))
        if tmp in ans:
          continue
        ans.append(tmp)

print(list(ans))
