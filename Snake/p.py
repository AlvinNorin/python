#!/usr/bin/python

import os

count = 0
usrInput = ['p.py', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
comment = None

while usrInput[count] != '' :
	usrInput[count] = raw_input("Add: ")
	count += 1
Max = count
count = 0
while count <= Max :
	os.system("git add "+usrInput[count])
	count += 1
comment = raw_input("Comment: ")
os.system("git commit -m \""+comment+"\"")
os.system("git push origin master")

