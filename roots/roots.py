import math
def roots(num1,num2,num3):
    r = num2**2 - (4 * num1 * num3)
    
    if r > 0:
        x1 = ((-1*num2) + math.sqrt(r)) / (2*num1)
        x2 = ((-1*num2) - math.sqrt(r)) / (2*num1)
        print("There are 2 roots: %f and %f" % (x1, x2))
        
    if r == 0:
        x1 = ((-1*num2) + math.sqrt(r)) / (2*num1)
        print("There is one root: ", x1)
    if r < 0:
       
       print("No roots, discriminant < 0.")
        

def run():
    start = True
   
    while start:
        a = float(input("Please Enter a ==> "))
        b = float(input("Please Enter b ==> "))
        c = float(input("Please Enter c ==> "))
        roots(a,b,c)
        
     
     
            
run()