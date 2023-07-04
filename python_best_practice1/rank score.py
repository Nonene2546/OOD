print(" *** Rank score ***")
arr = [x for x in input("Enter ID and Score end with ID : ").split()]
n = arr[-1]
del arr[-1]
print(arr)
print(n)
d = {}
for i in range(0, len(arr), 2):
  d[arr[i]] = float(arr[i+1])
print(d)
d = sorted(d.items(), key=lambda kv:(kv[0], kv[1]))
cnt = 0
for i in d:
  cnt += 1
  if i[0] == n:
    print(cnt)
    exit(0)