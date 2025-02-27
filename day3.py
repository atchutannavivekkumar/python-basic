#ifs 
num1 = int(input("enter no 1: "))
num2 = int(input("enter no 2: "))

if num1 == num2:
    print(" The both numbers({},{})are equal".format(num1,num2))
elif num1 < num2:
    print("{} is less than {}".format(num1,num2))
else:
    print("{} is less than {}".format(num2,num1))
3