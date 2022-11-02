def dividers(n):
    all_num = []
    for i in range(1,n):
        if n % i == 0 or n / i == n:
            all_num.append(i)
    
    return sum(all_num)


print(dividers(12))
print(dividers(8))