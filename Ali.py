print("comands:+, - , / , * .")

y=["+","-","/","*"]

for i in y:
  q=[]
  ask=input().split(i)
  q.append(ask)
  x=int(q[0][0])
  y=int(q[0][1])
  if i=="+":
    print(x+y)
  elif i=="-":
    print(x-y)
  elif i=="*":
    print(x*y)
  elif i=="/":
    print(x/y)
  else:
    print("oops!")
  break  
