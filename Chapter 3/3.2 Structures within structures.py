# -*- coding: cp1252 -*-

name = "John"
password = "ABC123"

name_input = input("Give name:")

if name_input == name:
	password_input = input("Give password:")
	if password_input == password:
		print("Both inputs are correct!")
	else:
		print("The password is incorrect.")
else:
	print("The given name is wrong.")
				  