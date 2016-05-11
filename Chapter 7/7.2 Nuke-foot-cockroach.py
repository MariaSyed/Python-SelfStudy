 # -*- coding: cp1252 -*-

import random	

def userchoice():
	usrchoice = input("Foot, Nuke or Cockroach? (Quit ends) : ")
	if usrchoice == "Foot":
		print("You chose: Foot")
		return 1
	elif usrchoice == "Nuke":
		print("You chose: Nuke")
		return 2
	elif usrchoice == "Cockroach":
		print("You chose: Cockroach")
		return 3
	elif usrchoice == "Quit":
		return 4
	else:
		
		return 5


def compchoice():
	compchoice = random.randint(1,4)
	if compchoice == 1:
		print("Computer chose: Foot")
	elif compchoice == 2:
		print("Computer chose: Nuke")
	elif compchoice == 3:
		print("Computer chose: Cockroach")
	return 	compchoice

def main():
	rounds = 0
	wins = 0
	ties = 0
	
	while True:
		usrnum = userchoice()
		if usrnum == 5:
			print("Incorrect selection.")
			usrnum = userchoice()
		if usrnum == 4:
			print("You played ", rounds ," rounds, and won ",wins," rounds, playing tie in ",ties,"rounds.")
			break
		compnum = compchoice()
		if usrnum == 1 and compnum == 3 or usrnum == 2 and compnum == 1 or usrnum == 3 and compnum == 2:
			print("You WIN!")
			wins = wins + 1
		elif compnum == 1 and usrnum == 3 or compnum == 2 and usrnum == 1 or compnum == 3 and usrnum == 2:
			print ("You LOSE!")
		elif usrnum == compnum:
			if usrnum == 2 and compnum == 2:
				print("Both LOSE!")
			else:
				print("It is a tie!")
				ties = ties + 1
		
		rounds = rounds + 1
		


if __name__=="__main__":
	main()