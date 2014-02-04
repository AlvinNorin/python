#!/usr/bin/python

import os

os.system("git config --global credential.helper cache")

def push() :
	comment = None
	os.system("cd && cd python && git add Snake")
	comment = raw_input("Comment: ")
	os.system("git commit -m \""+comment+"\"")
	os.system("git push origin master")

def pull() :
	os.system("git pull")

while True :
	usrInput = raw_input("\n1) Push\n2) Pull\n(")
	if str(usrInput) == '1' :
		push()
	elif str(usrInput) == '2' :
		pull()
