number = int(input("enter number"))

list = [int(x) for x in str(number)]
print(list)
l = 0
print(len(list))

for r in range(len(list)):
    if list[l] > list[r]:
        pass
    if list[r] > list[l]:
       list[r], list[l] = list[l], list[r]
      
       r = r+ 1 
l=l+1
for r in range(l,len(list)):
    if list[l] > list[r]:
        pass
    if list[r] > list[l]:
       list[r], list[l] = list[l], list[r]
      
       r = r+ 1
 
print(list)


print(sorted(list)[::-1])
for x in range(len(list)):
    print (sorted(list)[::-1][x], end="")