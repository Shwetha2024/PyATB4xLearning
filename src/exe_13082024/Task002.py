"""Create a program , take 2 inputs from the user num1, num2 and give them
max
pow num1 to num2
sub, mul, sum, div.
Format your out with f{""}"""

number1 = int(input("Enter a number of your choice: "))
number2 = int(input("Enter a another number of your choice: "))
highest = max(number1, number2)
print(f"Maximun of {number1} and {number2} is {highest}")

result=pow(number1,number2)
print(f"Power of {number1} and {number2} is {result}")

print(f"The sum of {number1} and {number2} is {number1+number2}")
print(f"The product of {number1} and {number2} is {number1*number2}")
print(f"The difference of {number1} and {number2} is {number1-number2}")
print(f"The division of {number1} and {number2} is {number1/number2}")

print(f"formatted {number1} is {number1:.3f}")
print(f"formatted {number2} is {number2:.4f}")

