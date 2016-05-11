def powerof(number):
	return 2 ** number

def main():
	user_input = int(input("Give a number: "))
	result = powerof(user_input)
	print("The result is ",result)
	
if __name__ == "__main__":
	main()