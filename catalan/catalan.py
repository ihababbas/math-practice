def factorin(number):
    fact = 1
    if number < 0:
        return "Wrong input" 
    if number == 1 or number == 0:
        return 1
    else:
        for i in range(1,number+1):
            fact = fact * i
    return fact

print(factorin(5))


def catalan(number):
    if number < 0:
        return "Wrong input" 
    
    
    else:
        resulte = factorin(2*number) / (factorin(number)* factorin(number +1))
        
    return resulte


for n in range(10):
    print(catalan(n))   
    
    