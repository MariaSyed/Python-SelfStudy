# -*- coding: cp1252 -*-

print("Calculator")

number1 = int(input("Give the first number:"))
number2 = int(input("Give the second number:"))


print("""(1) +
(2) -
(3) *
(4) /""")

user_select = input("Please select something (1-4):")

if user_select == "1":
	result = number1 + number2
	print("The result is:",result)
elif user_select == "2":
	result = number1 - number2
	print("The result is:",result)
elif user_select == "3":
	result = number1 * number2
	print("The result is:",result)
elif user_select == "4":
	result = number1 / number2
	print("The result is:",result)
else:
	print("Selection was not correct.")

