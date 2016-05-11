 # -*- coding: cp1252 -*-

readfile = open("facts.txt","r")
content = readfile.read()
print("Following was read from the file: ",content)
readfile.close()
