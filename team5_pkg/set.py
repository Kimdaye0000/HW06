#!/usr/bin/python3

def set_run():
	print("input the 1st list : ",end='')
	
	s1 = set(map(lambda x: int(x), input().split()))
	
	print("input the 2st list : ",end='')
	s2 = set(map(lambda x: int(x), input().split()))
	
	u = list(s1 | s2)
	i = list(s1 & s2)
	
	print("union : [",end='')
	if u:
		for n in range(0, len(u) - 1):
			print(u[n], end=',')
		print("%d]" % u[-1])
	else:
		print("]")
	
	print("intersection : [", end='')
	if i:
		for n in range(0, len(i) - 1):
			print(i[n], end=',')
		print("%d]" % i[-1])
	else:
		print("]")

if __name__ == '__main__':
	set_run()

