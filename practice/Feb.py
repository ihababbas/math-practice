def largerthanthosand(x ,y):
    maulti = x * y
    
    if maulti > 1000:
        return x + y
    return maulti


# print(largerthanthosand(20,30))
# print(largerthanthosand(40,30))


def sumofpreivous(x):
    if x < 0:
        return "less than zero"
    for i in range(x):
        print ('the number :' ,i  ,' is privous :' ,i-1 , "the sum of :" , i + (i-1))
    
# sumofpreivous(10)  
# sumofpreivous(2)   


def oddindex(x):
    for i in range(1,len(x),2):
        print(x[i])
        
def partofstring(x,n):
    for i in range(n,len(x)):
        print(x[i])
    
    
    
    
# oddindex("ihab")
# partofstring("pynative",2)


def pattern(x):
    row = x
    count = 0
    for j in range(row):
        for i in range(j):
            print (count, end=" ") 
        print("\n")
        count = count + 1
        
        
    # count = 0
    # for num in range(x):
    #     for i in range(num):
    #         print (count, end=" ") 
    #     print("\n")
    #     count = count + 1
        
pattern(3)

def Palindrome(x):
    
    num = x
    reverse = int(str(num)[::-1])

    if num == reverse:
        print('Palindrome')
    else:
        print("Not Palindrome")
    

Palindrome(121)
Palindrome(1223)

def newList(list1, list2):
    nlist = []
    for i in range(len(list1)):
        if list1[i] % 2 == 1:
            nlist.append(list1[i])
            
    for i in range(len(list2)):
        if list2[i] % 2 == 0:
            nlist.append(list2[i])
            
    print(nlist)
    
list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]    
newList(list1, list2)


from datetime import datetime

# Time object containing
# the current time.
time = datetime.now().time()

print("Current Time =", time)
