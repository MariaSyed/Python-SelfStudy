import time

userinput = ""

while True:
	try:
		myfile=open("notebook.txt","r")
	except IOError:
		print("No default notebook was found, created one.")
		notebook="notebook.txt"
		myfile=open(notebook,"w")
	else:
		print("Now using file "+notebook+"\n(1) Read the notebook\n(2) Add note\n(3) Empty the notebook\n(4) Change the notebook\n (5) Quit\n")
		userinput = input("Please select one: ")
		if userinput == "1":
			myfile = open(notebook,"r")
			content = myfile.read()
			print(content)
			myfile.close()
		elif userinput == "2":
			myfile = open(notebook, "a")
			addedtext = input("Write a new note: ")
			addedtext = addedtext + ":::" + time.strftime("%X %x")
			myfile.write(addedtext)
			myfile.close()
		elif userinput == "3":
			myfile = open(notebook, "w")
			print("Notes deleted." + ":::" + time.strftime("%X %x"))
			myfile.close()
		elif userinput == "4":
			notebook=input("Give the name of the new file: ")
			try:
				myfile=open(notebook,"r")
			except IOError:
				print("No notebook with that name detected, created one.")
				mylife=open(notebook,"w")
				
		elif userinput == "5":
			keepgoing = False
			print("Notebook shutting down, thank you.")
			myfile.close()
			break