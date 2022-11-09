import math


def red(a,b):
    r = math.sqrt((a**2)+(b**2))
    return r
    
    


def Q1():
    start = True
    all_cicle=[]
    while start:
        num1 = int(input("Please Enter num1 ==> "))
        num2 = int(input("Please Enter num2 ==> "))
        all_cicle.append(red(num1,num2))
        if red(num1,num2) == 0:
            print(max(all_cicle))
            start = False
            
#Q1()

def Q2():
    start = True
    count = 0
    num2 = 0
    num1 = float(input("Please Enter num1 ==> "))
    ceil = math.ceil(num1)
    ceil = ceil+1

    while start:
        for x in range(-ceil,ceil):
            for y in range(-ceil,ceil):
                num2 = red(x,y)
                if num1 >= num2:
                    count = count+1
                else:
                    start = False
    print(count)   
       
     
Q2()