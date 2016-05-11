mylist = []
while True :
	user_input = int(input("""Would you like to
	(1)Add or
	(2)Remove items or
	(3)Quit?:"""))
	
	if user_input == 1:
		add_input = input("What will be added?: ")
		mylist.append(add_input)
	
	elif user_input == 2:
		print("There are ",len(mylist), " items in the list.")
		try:
			mylist.pop(int(input("Which item is deleted?: ")))
		except Exception:
			print("Incorrect selection.")
	
	elif user_input == 3:
		print("The following items remain in the list: ")
		for i in mylist:
			print(i)
		break
	
	else:
		print("Incorrect selection. ")
		
