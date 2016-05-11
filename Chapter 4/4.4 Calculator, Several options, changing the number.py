# -*- coding: cp1252 -*-

print("Calculator")
number1 = int(input("Give the first number:"))
number2 = int(input("Give the second number:"))
key = True

while key == True:
	print("""(1) + 
(2) - 
(3) * 
(4) / 
(5)Change numbers 
(6)Quit""")
	print("Current numbers: ",number1,number2)
	selection = input("Please select something (1-6): ")
	
	if selection == "1":
		result = number1 + number2
		print("The result is: ",result)
	elif selection == "2":
		result = number1 - number2
		print("The result is: ",result)
	elif selection == "3":
		result = number1 * number2
		print("The result is: ",result)
	elif selection == "4":
		result = number1 / number2
		print("The result is: ",result)
	elif selection == "5":
		number1 = int(input("Give the first number:"))
		number2 = int(input("Give the second number:"))
	elif selection == "6":
		print("Thank you!")
		key = False
	
	
		