number = int(input("Enter a number: "))

smallest = number

number = int(input("Enter another number: "))

if number < smallest:
  smallest = number
  
duck = int(input("Enter another number: "))
if duck < smallest:
  smallest = duck

print("The smallest number is ", smallest)
