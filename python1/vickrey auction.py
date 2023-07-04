occ = {}
x = [int(i) for i in input("Enter All Bid : ").split()]
for i in x:
  if i in occ:
    occ[i] += 1
  else:
    occ[i] = 1

mx = max(occ)
if len(occ) < 2:
  print("not enough bidder")
  exit(0)
if occ[mx] > 1:
  print("error : have more than one highest bid")
  exit(0)
del occ[mx]
mx2 = max(occ)
print(f'winner bid is {mx} need to pay {mx2}')
