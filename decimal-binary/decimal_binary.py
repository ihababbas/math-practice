def DtoB(number):
    if number > 1:
        DtoB(number//2)
    print(number%2,end="")
    
def BtoD(number):
    sum = 0
    my_list = [int(x) for x in str(number)]
    my_list.reverse()
    for n in range(len(my_list)):
        if my_list[n] == 1:
            sum = sum + 2**n
    
    print(sum)           



DtoB(78)
print("\n")
BtoD(1001110)