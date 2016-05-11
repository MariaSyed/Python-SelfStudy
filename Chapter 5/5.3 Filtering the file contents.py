  # -*- coding: cp1252 -*-

file = open("strings.txt","r")
content = file.readlines()

for line in content:
	if line[:-1].isalnum():
		print(line[:-1]," was ok.")
	else:
		print(line[:-1]," was invalid.")

file.close()