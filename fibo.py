#!/usr/bin/python3

num = [0, 1, 0]
i = 0
n = 2
i = int(input("fibonacci number : "))

if i >= 2:
    print(f"{num[1]}",end=' ') 
    while n <= i:
       num[2] = num[1] + num[0]
       num[0] = num[1]
       num[1] = num[2]
       n += 1
       print(f"{num[1]}",end=' ')	
else:
    print("Error : 2 이상의 자연수를 입력해주세요.")
print(end='\n') 
print(f"F{i} = {num[2]}")


