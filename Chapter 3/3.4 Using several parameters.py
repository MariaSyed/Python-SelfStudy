input1 = int(input("Give a number:"))
input2 = int(input("Give another number:"))

if (input1 % 2 == 0) and (input2 % 2 == 0):
	print("Both numbers are even.")
if ((input1 % 2 == 0) and (input2 % 2 != 0)) or ((input1 % 2 != 0) and (input2 % 2 == 0)):
	print("One of the numbers is even.")
if (input1 % 2 != 0) and (input2 % 2 != 0):
	print("Both numbers are odd.")