#!/usr/bin/python

import os
import time

os.system("git config --global credential.helper cache")
os.system("git config --global credential.helper 'cache --timeout=3600'")

def push() :
	comment = None
	os.system("cd && cd python && git add Snake")
	comment = raw_input("Comment: ")
	os.system("git commit -m \""+comment+"\"")
	os.system("git push origin master")

def pull() :
	os.system("git pull")

def autoPull() :
	while True :
		os.system("git pull")
		time.sleep(10)

while True :
	usrInput = raw_input("\n1) Push\n2) Pull\n3) Automatic pull\n(")
	if str(usrInput) == '1' :
		push()
	elif str(usrInput) == '2' :
		pull()
	elif str(usrInput) == '3' :
		autoPull()
