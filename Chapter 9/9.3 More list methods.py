readfile = open("words.txt","r")
content = readfile.readlines()
mylist = content
mylist.sort()
print("Words in an alphabetical order: ")
for i in mylist:
	print(i)
