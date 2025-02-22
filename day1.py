#exercise 1 
#patientName = input("what is the name ")
#patientAge = input("what is your age ")
 
#print(patientName)
#print(patientAge)

#excercise 2

#firstNumber = int(input("Enter the first number: "))
#secondNumber = float(input("enter the seconf number: "))

#sum = firstNumber+secondNumber

#print(sum)

#excercise 3

PersonWeight = int(input("Enter your Weight: "))
unitsWeight = str(input("If the weight is in kg enter K and if in Lbs enter L: "))

if unitsWeight =="l":
    PersonWeightlbs = PersonWeight/(2.2)
    print(PersonWeightlbs)
else:
    print(PersonWeight)
