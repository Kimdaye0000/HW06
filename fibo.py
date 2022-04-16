#!/usr/bin/python3

num = [0, 1, 0]
n = 2
i = int(input("fibonacci number : "))

if i >= 1:
    while n <= i:
       print(f"{num[1]}",end=' ')
       num[2] = num[1] + num[0]
       num[0] = num[1]
       num[1] = num[2]
       n += 1
    print(f"{num[1]}")
    print(f"F{i} = {num[1]}")
else:
    print("Error : 1 이상의 자연수를 입력해주세요.")
