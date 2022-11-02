def dividers(n):
    all_num = []
    for i in range(1,n):
        if n % i == 0 or n / i == n:
            all_num.append(i)
    
    return sum(all_num)


def is_abundant(sum_div,num):
    if sum_div > num:
        return True
    else:
        return False
    
    




print(dividers(12))
print(dividers(8))
print(is_abundant(dividers(12),12))
print(is_abundant(dividers(8),8))


