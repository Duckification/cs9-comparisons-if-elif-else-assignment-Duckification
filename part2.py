num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
num3 = int(input("Enter another number: "))

if(num1 == num2 == num3):
  print("All three numbers are equal.")

elif(num1 == num2 or num2 == num3 or num1 == num3):
  print("Exactly two of the numbers are equal.")

else: 
  print("None of the numbers are equal.")
