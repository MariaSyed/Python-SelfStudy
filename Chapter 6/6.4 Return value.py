def response(givenstring):
	if len(givenstring) < 10:
		print("Too short")
	else:
		print(givenstring)
		if "X" in givenstring:
			print("X spotted!")
			

def main():
	while True:
		userInput = input("Write something (quit ends): ")
		if userInput == "quit":
			break
			
		else:
			response(userInput)
			
if __name__ == "__main__":
	main()