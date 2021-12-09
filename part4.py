num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
if(num1 == 0):
  print("zero")
elif(num2 == 0):
  print("zero")
elif(num1 > 0 and num2 > 0):
  print("positive")
elif(num1 <= 0 and num2 <= 0):
  print("negative")
elif(num1 > 0 and num2 <= 0):
  print("opposite")
elif(num1 <= 0 and num2 > 0):
  print("opposite")
