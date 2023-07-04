print("*** Rabbit & Turtle ***")
d, vr, vt, vf = [int(x) for x in input("Enter Input : ").split()]
t1 = d / (vt - vr)
print("{:.2f}".format(vf * t1))