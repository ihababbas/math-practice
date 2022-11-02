def sum_difference(n):
    sum_of_squares = 0
    square_of_sum = 0
    for i in range(n):
        squares = i*i
        sum_of_squares = sum_of_squares + squares
        square_of_sum = square_of_sum + i
        
    square_of_sum = square_of_sum**2
    return  square_of_sum-sum_of_squares
    
    
    
    
print(sum_difference(5))
