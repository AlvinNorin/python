#!/usr/bin/python

import os

def push() :
	comment = None
	os.system("cd && cd python && dir && git add Snake")
	comment = raw_input("Comment: ")
	os.system("git commit -m \""+comment+"\"")
	os.system("git push origin master")

while True :
	usrInput = raw_input("1) Push\n2) Pull\n")
	if str(usrInput) == '1' :
		push()
	elif usrInput == 2 :
		pull()