def comment(givenstring):
	if len(givenstring) < 10:
		print("Too short")
	else:
		print(givenstring)

def main():
	while True:
		userinput = input("Write something (quit ends) : ")
		if userinput == "quit":
			break
		else:
			comment(userinput)

if __name__ == "__main__" :
	main()	