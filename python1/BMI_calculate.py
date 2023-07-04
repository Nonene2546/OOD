h, w = [float(x) for x in input("Enter your High and Weight : ").split()]
BMI = w / (h*h)
if(BMI < 18.5):
    print("Less Weight")
elif(BMI < 23):
    print("Normal Weight")
elif(BMI < 25):
    print("More than Normal Weight")
elif(BMI < 30):
    print("Getting Fat")
else:
    print("Fat")