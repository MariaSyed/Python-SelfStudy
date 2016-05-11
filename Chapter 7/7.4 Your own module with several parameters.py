# -*- coding: cp1252 -*-

def testme(password):
	if len(password) > 6 and str.isalnum(password) and (not str.isdigit(password)) and (not str.isalpha(password)):
		return True
	else:
		return False