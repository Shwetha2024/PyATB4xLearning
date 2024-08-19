
'''Write a Python program to calculate the area of a circle given its radius using the
formula ``` area=π×r^2``` ( Take pie as 3.14)'''

import math

R= float(input("Enter the radius of the circle"))
print (R)
print (r"Choose if pi=3.14 or from math.pi")
choice=input("Enter the radius of the circle")
if choice=='3.14':
    pi_value=3.14
    print(pi_value)
else:
    pi_value =math.pi
    print(pi_value)
area=pi_value*pow(R,2)
print("Area of the circle with radius",R,f"is {area:.4f}")



