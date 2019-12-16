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
print("comands:+, - , / , * .")
ask=input().split()
all=calc(int(ask[0]),ask[1],int(ask[2]))
print(all)
#this is my code
