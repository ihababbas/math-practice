def primelist(number):
    if number == 1:
        return 0
    limit = number+1
    not_prime_number = set()
    prime_numbers = []
    
    for i in range(2,limit):
        if i in not_prime_number:
            continue
        
        for f in range(i*2, limit,i):
            not_prime_number.add(f)
            
        prime_numbers.append(i)
    x = len(prime_numbers)
    return prime_numbers

    
def primelistforlist(number):
    if number == 1:
        return 0
    limit = number+1
    not_prime_number = set()
    prime_numbers = []
    
    for i in range(2,limit):
        if i in not_prime_number:
            continue
        
        for f in range(i*2, limit,i):
            not_prime_number.add(f)
            
        prime_numbers.append(i)
    x = len(prime_numbers)
    if prime_numbers[x-1] == number:
      return prime_numbers[x-1]
    else:
        return 0

print(primelist(225))

list = [1, 3, 4, 7, 9]
sum = 0
if len(list) == 0:
    print("Empty list")
else:
    for x in range(len(list)):
      sum= sum+ primelistforlist(list[x])
    
print(sum)
    

