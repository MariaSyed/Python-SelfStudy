import math

print("Calculator")
keepgoing = True

while keepgoing:
	try:
		num1 = input("Give a number: ")
		num1 = int(num1)
		break
		
	except ValueError:
		print("This input is invalid.")
		
while keepgoing:
	try:
		num2 = input("Give a number: ")
		num2 = int(num2)
		break
		
	except ValueError:
		print("This input is invalid.")

while keepgoing:	
	print("(1) +\n(2) -\n(3) *\n(4) /\n(5) sin(number1/number2)\n(6) cos(number1/number2)\n(7) Change numbers\n(8) Quit\n")
	print("Current numbers:" , num1,num2)
	value = int(input("Please select something (1-6): "))
	if value == 1:
		print("The result is:" ,num1+num2)
	elif value == 2:
		print("The result is:" ,num1-num2)
	elif value == 3:
		print("The result is:" ,num1*num2)
	elif value == 4:
		print("The result is:" ,num1/num2)
	elif value == 5:
		print("The result is:" , math.sin(num1/num2))
	elif value == 6:
		print("The result is:" , math.cos(num1/num2))
	elif value == 7:
		while keepgoing:
			try:
				num1=input("Give a number: ")
				num1=int(num1)
			except ValueError:
				print("This input is invalid.")
				
		while keepgoing:
			try:
				num2=input("Give a number: ") 
				num2=int(num2)
			except ValueError:
				print("This input is invalid.")
		
	elif value == 8:
		print("Thank you!")
		keepgoing = False
		break
