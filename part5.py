month = input("Enter a month: ")

if(month == "January" or month == "january" or month == "March" or month == "march" or month == "may" or month == "May" or month == "July" or month == "july" or month == "August" or month == "august" or month == "october" or month == "October" or month == "December" or month == "december"):
  print("31")
elif(month == "February" or month == "february"):
  print("28")
elif(month == "April" or month == "april" or month == "June" or month == "june" or month == "september" or month == "September" or month == "november" or month == "November"):
  print("30")
else:
  print ("learn yo months ")
