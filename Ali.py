  def calc(x,y,z):
  if y=="+":
    return(x+z)
  elif y=="-":
    return(x-z)
  elif y=="/":
    return(x/z)
  elif y=="*":
    return(x*z)
  else:
    return("oops!")
x = int(input("1st num: "))
z = int(input("2st num: "))
y = input("operation: ")
print calc(x,y,z)
