# different kind of user defined functions


#1 No Return and no argument/parameter

def NRNP():
    print("NRNP")

result= NRNP()
print(result)

#2 No return with argument

def NRWA(name):
    print("Hello,",name)

result1= NRWA("Test")
print(result1)

#name=input("Enter the name to be displayed\n")
#NRWA(name)

#3 NO return with default Argument
def NRWD(name="World"):
    print("Hello,",name)

result2= NRWD()
print(result2)

def NRWD2(name1="Toy", name2="Story"):
    print("Hello", name1, name2)

NRWD2(name2="Star")
NRWD2 ()
NRWD2("Krish", "VI")

#4 return with Argument

def RWA(num1=3,num2=6):
    return num1*num2

result3=RWA(5,8)
print(result3)


