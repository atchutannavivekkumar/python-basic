#functions

#basic
def func1():
    print("I am a function")

#defining arguments
def func2(arg1, arg2):
    print(arg1, " ", arg2)

#return value
def func3(x):
    return x*x*x 

#power and loop 
def func4(num, x=1):
    result = 1
    for i in range (x):
        result = num * result
    return result

#multiarguments

def func5(*args):
    result = 0
    for x in args:
        result = result + x
    return result





#calling
#func1()
#print(func1())

#func2(10,30)
#print(func2(10,30))

#func3(4)
#print(func3(4))

#func4(2,3)
#print(func4(2,3))

numt = int(input("enter a number: "))
func5(1,2,3,4,5,6,numt)
print(func5(1,2,3,4,5,6,numt)
)