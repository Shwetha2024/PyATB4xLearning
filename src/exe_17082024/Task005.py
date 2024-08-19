### Task #5
'''Create a program that takes two numbers as input and prints whether the first number
 is greater than, less than, or equal to the second number.'''

R1= float(input("Enter the first number"))
print (R1)
R2= float(input("Enter the second number"))
print (R2)
if R1==R2:
    print (f"{R1:.0f} equals {R2:.0f}")
elif R1 > R2:
    print(R1, "greater than", R2)
else:
    print(R1, "lesser than", R2)
