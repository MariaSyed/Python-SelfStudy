 # -*- coding: cp1252 -*-

filename = input("Give a file name: ")
content = input("Write something: ")
file = open(filename,"w")
file.write(content)
file.close
print("Wrote ",content,"to the file ",filename)