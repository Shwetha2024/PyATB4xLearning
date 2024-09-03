#max of 3 numbers
N1=int(input("Enter first number\n"))
N2=int(input("Enter second number\n"))
N3=int(input("Enter third number\n"))

if N1>=N2 and N1>=N3:
    print("Max number is", N1)
elif N2>=N1 and N2>=N3:
    print("Max number is", N2)
else:
    print("Max number is", N3)

