a= "first_number"
b= "sec_number"

print ("your first number is" + str(a))
print ("your second number is" + str(b))

print('''make your choice 
      print 1 for addition 
      print 2 for subtration
      print 3 for multiplying
      print 4 for division''')
c= int(input("enter your choice"))

print(type(c))

if c==1:
  result =a+b
  print result 
elif c==2:
  result= a-b
  print result 
elif c==3:
  result =a*b
  print result 
elif c==4:
  result=a/b
  print result 
else:
  print error

      
