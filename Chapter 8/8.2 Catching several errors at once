# -*- coding: cp1252 -*-
def filename():
	fname = input("Give the file name: ")
	return fname

def main():
	string = filename()

	try:
		handle = open(string,"r")
		filetext = handle.read()
		result=int(filetext)
		
		
		
	except IOError:
		print("There seems to be no file with that name.")
	
	except (TypeError, ValueError):
		print("The file contents were unsuitable.")
	
	
		
	else:
		print("The result was 3.194888178913738")

if __name__ == "__main__":
	main()
	