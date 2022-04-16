#!usr/bin/python3

import team5_pkg

while True:
	try:
		sel = int(input('Select menu: 1)b2h 2)set 3)fibo 4)exit ? '))
	except ValueError:
		print('input is not a number')
		continue
	if sel == 1:
		team5_pkg.convertToHex()
	elif sel == 2:
		team5_pkg.set_run()
	elif sel == 3:
		team5_pkg.fibo_run()
	elif sel == 4:
		print('exit the program...')
		break
	else:
		print('menu does not exist')
	print()
