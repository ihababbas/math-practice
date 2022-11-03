def primelist(number):
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


print(primelist(15))