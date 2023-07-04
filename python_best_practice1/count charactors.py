print(" *** String count ***")
s = input("Enter message : ")
lower=0
upper=0
lower_list = []
upper_list = []
for i in s:
      if(i.islower()):
            lower+=1
            lower_list.append(i)
      elif(i.isupper()):
            upper+=1
            upper_list.append(i)

lower_list = set(lower_list)
upper_list = set(upper_list)
lower_list = sorted(lower_list)
upper_list = sorted(upper_list)
print('No. of Upper case characters : ' + str(upper))
print('Unique Upper case characters : ' + '  '.join(upper_list))
print('No. of Lower case Characters : ' + str(lower))
print('Unique Lower case characters : ' + '  '.join(lower_list))
