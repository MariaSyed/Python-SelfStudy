# -*- coding: cp1252 -*-

key = True

while key == True:
	user_input = input("Write something:")
	
	if user_input == "quit":
		print("Bye bye!")
		key = False
	
	else:
		print(user_input)