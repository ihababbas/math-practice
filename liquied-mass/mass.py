import math


def volume(r):
    pi = math.pi
    vol = (4.0/3.0) * pi * r**3
    return vol

def mass(x,y):    
    m = (x * y) / 2.0
    return m

def run():
    start = True
    all_mass=[]
    while start:
        redius = float(input("Please Enter Redius ==> "))
        density = float(input("Please Enter Density ==> "))
        new_mass = mass(volume(redius),density)
        if new_mass == 0:
            print(f'mass = {new_mass}')
            print(f'the highest mass is ,{max(all_mass)}')
            start = False
        else:
            print(f'mass = {new_mass}')
            all_mass.append(new_mass)
     
     
            
run()