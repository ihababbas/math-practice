number = int(input("enter number"))

list = [int(x) for x in str(number)]
print(list)
l = 0
print(sorted(list)[::-1])
for x in range(len(list)):
    print (sorted(list)[::-1][x], end="")

