#!/usr/bin/python3

import b2h
import set
import fibo

while True:
	try:
		sel = int(input('Select menu: 1)b2h 2)set 3)fibo 4)exit ? '))
	except ValueError:
		print('Invalid input : enter a number only')
		continue
	if sel == 1:
		b2h.run()
	elif sel == 2:
		set.run()
	elif sel == 3:
		fibo.run()
	elif sel == 4:
		print('exit the program...')
		break
	else:
		print('Invalid menu')
	print()
