#question 1 
#Q1: Write a Python program that prints the numbers from 1 to 10 using a for loop.

#for i in range(1,11):

#    print(i)

#question 2
#Q2: Write a Python program that prints the even numbers from 2 to 20 using a while loop.

#i = 0

#while i<21:
 #   i = i+1
  #  if i % 2 ==0:
   #     print(i)
    #else:
     #   print("not even")

#question 3
#Q3: Write a Python program that takes a number as input and prints its multiplication table up to 10 using a for loop.
#num1 = int(input("enter number for multiplication: "))
#num2 = int(input("Enter the number you want to multiply untill: "))


#for i in range(1,num2+1):
 #   mul = num1 * i
  #  print("{} X {} = {}".format(num1,i,mul))

#question 4

#Q4: Write a Python program that calculates the sum of all numbers from 1 to n, where n is given as input, using a while loop.

num1 = int(input("Enter the no untill you want sum: "))

j=0
i = 1

while i <= num1:
    j = j+i  # Add current number to sum
    i = i+1 

print("The sum of 1 to {} is {}".format(num1,j))


    
