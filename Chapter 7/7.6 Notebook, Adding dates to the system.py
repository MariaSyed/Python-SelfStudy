import time

userinput = ""
keepgoing = True
while keepgoing:
	print("(1) Read the notebook\n(2) Add note\n(3) Empty the notebook\n(4) Quit")
	userinput = input("Please select one: ")
	if userinput == "1":
		myfile = open("notebook.txt","r")
		content = myfile.read()
		print(content)
		myfile.close()
	elif userinput == "2":
		myfile = open("notebook.txt", "a")
		addedtext = input("Write a new note: ")
		addedtext = addedtext + ":::" + time.strftime("%X %x")
		myfile.write(addedtext)
		myfile.close()
	elif userinput == "3":
		myfile = open("notebook.txt", "w")
		print("Notes deleted." + ":::" + time.strftime("%X %x"))
		myfile.close()
	elif userinput == "4":
		keepgoing = False
		print("Notebook shutting down, thank you.")
		myfile.close()
	else:
		print("Wrong input")