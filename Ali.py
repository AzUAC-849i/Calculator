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
    return("Oops!")
print("Commands: +, - , / , * ")
ask=input().split()
all=calc(float(ask[0]),ask[1],float(ask[2]))
print(all)
