#!/usr/bin/python3

## bin to hex convesion

def convertToHex():
    
    checkisB = {'0','1'}
    num = input("input bin number : ")
    dedupe = set(num)
    
    if checkisB == dedupe or dedupe == {'0'} or dedupe == {'1'}:
        print("hexa number :",f'{int(num,2):#010x}')
        
    else:
        print("wrong input you can input binary only")
    
if __name__ == '__main__':
    convertToHex()
