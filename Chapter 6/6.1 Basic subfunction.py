def hello():
	""" Prints "Hello There" """
	print("Hello there!")

def main():
	""" Prints something """
	print("Lets call the subfunction:")
	hello()
	print("Quitting.")
	
if __name__ == "__main__":
	main()