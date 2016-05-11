import math

def main():
	print("Calculator")
	num1 = int(input("Give the first number: "))
	num2 = int(input("Give the second number: "))
	
	while True:
		print("""(1) +
(2) -
(3) *
(4) /
(5)sin(number1/number2)
(6)cos(number1/number2)
(7)Change numbers
(8)Quit""")
		print("Current numbers: ",num1," ", num2)
		selection = int(input("Please select something (1-6): "))
		if selection == 1:
			result = num1 + num2
			print("The result is: ",result)
		elif selection == 2:
			result = num1 - num2
			print("The result is: ",result)
		elif selection == 3:
			result = num1 * num2
			print("The result is: ",result)
		elif selection == 4:
			result = num1 / num2
			print("The result is: ",result)
		elif selection == 5:
			result = math.sin(num1/num2)
			print("The result is: ",result)
		elif selection == 6:
			result = math.cos(num1/num2)
			print("The result is: ",result)
		elif selection == 7:
			num1 = int(input("Give the first number: "))
			num2 = int(input("Give the second number: "))
		elif selection == 8:
			print("Thank you!")
			break

			
if __name__ == "__main__":
	main()
		