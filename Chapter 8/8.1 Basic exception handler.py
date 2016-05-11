number = input("Give a number: ")

try:
	number = int(number)
	print("The input was suitable!")

except Exception:
	print("The input was malformed.")