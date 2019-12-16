print('Enter 1 for Adding\nEnter 2 for Substraction\nEnter 3 for Multpling \nEnter 4 for Dividing.')
main_q = input('I Want to:')

if main_q == '1':
  print('Enter Numbers For Adding')
  given1 = input('Enter 1st Number Here: ')
  given2 = input('Enter 2nd Number Here: ')
  try:
    numb1 = int(given1)
    numb2 = int(given2)
  except ValueError:
    print("Enter Numbers Only!")
    given1 = input('Enter 1st Number Here: ')
    given2 = input('Enter 2nd Number Here: ')
  else:
    print (numb1,'+',numb2,'=',numb1+numb2)

if main_q == '2':
  print('Enter Numbers For Substriction')
  given1 = input('Enter 1st Number Here: ')
  given2 = input('Enter 2nd Number Here: ')
  try:
    numb1 = int(given1)
    numb2 = int(given2)
  except ValueError:
    print("Enter Numbers Only!")
  given1 = input('Enter 1st Number Here: ')
  given2 = input('Enter 2nd Number Here: ')
  else:
    print (numb1,'-',numb2,'=',numb1-numb2)

if main_q == '3':
  print('Enter Numbers For Multiplying')
  given1 = input('Enter 1st Number Here: ')
  given2 = input('Enter 2nd Number Here: ')
  try:
    numb1 = int(given1)
    numb2 = int(given2)
  except ValueError:
    print("Enter Numbers Only!")
  given1 = input('Enter 1st Number Here: ')
  given2 = input('Enter 2nd Number Here: ')
  else:
    print (numb1,'*',numb2,'=',numb1*numb2)
    
if main_q == '4':
  print('Enter Numbers For Dividing')
  given1 = input('Enter 1st Number Here: ')
  given2 = input('Enter 2nd Number Here: ')
  try:
    numb1 = int(given1)
    numb2 = int(given2)
  except ValueError:
    given1 = input('Enter 1st Number Here: ')
    given2 = input('Enter 2nd Number Here: ')
    print("Enter Numbers Only!")
  else:
    print (numb1,'/',numb2,'=',numb1/numb2)
