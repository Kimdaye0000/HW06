#!/usr/bin/python3

num = [0, 1, 0]
<<<<<<< HEAD
n = 2
i = int(input("fibonacci number : "))

if i >= 1:
    while n <= i:
       print(f"{num[1]}",end=' ')
=======
i = 0
n = 2
i = int(input("fibonacci number : "))

if i >= 2:
    print(f"{num[1]}",end=' ') 
    while n <= i:
>>>>>>> 352c04885cd2de6415d32314df8e1a8e4ba1eb45
       num[2] = num[1] + num[0]
       num[0] = num[1]
       num[1] = num[2]
       n += 1
<<<<<<< HEAD
    print(f"{num[1]}")
    print(f"F{i} = {num[1]}")
else:
    print("Error : 1 이상의 자연수를 입력해주세요.")
=======
       print(f"{num[1]}",end=' ')	
else:
    print("Error : 2 이상의 자연수를 입력해주세요.")
print(end='\n') 
print(f"F{i} = {num[2]}")


>>>>>>> 352c04885cd2de6415d32314df8e1a8e4ba1eb45
