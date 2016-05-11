notebook = open("notebook.txt","w")
#notebook.write("Buy milk")

while True:
	print("""
(1) Read the notebook
(2) Add note
(3) Empty the notebook
(4) Quit
""")
	user_select = input("Please select one: ")
	
	if user_select == "1":
		notebook = open("notebook.txt","r")
		content = notebook.readlines()
		if len(content) == 0:
			notebook = open("notebook.txt","a")
			notebook.write("Buy milk\n")
			notebook = open("notebook.txt","r")
			content = notebook.readlines()
			for line in content:
				print(line[:-1])
			notebook.close()
			
		else:
			for line in content:
				print(line[:-1])
			notebook.close()
	
	elif user_select == "2":
		notebook = open("notebook.txt","a")
		new_note = input("Write a new note: ")
		notebook.write(new_note+"\n")
		notebook.close()
	
	elif user_select == "3":
		notebook = open("notebook.txt","w")
		notebook.close()
		print("Notes deleted.")
	
	elif user_select == "4":
		print("Notebook shutting down, thank you.")
		break
	
	else:
		print("Incorrect selection")
		