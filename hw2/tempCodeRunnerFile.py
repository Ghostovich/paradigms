number = int(input("Enter the number: "))     
def multiplication(number):
  print("The Multiplication Table of: ", number)   
  for count in range(1, 10):     
    print(number, 'x', count, '=', number * count)   

multiplication(number)