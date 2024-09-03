# Triangle classifier

A=int(input("Enter the length of the first side of the triangle\n"))
B=int(input("Enter the length of the second side of the triangle\n"))
C=int(input("Enter the length of the third side of the triangle\n"))

if (A==B and B==C):###A==B==C
    print("Triangle is equilateral")
elif(A==B or B==C or A==C):
    print("Triangle is isosceles")
else:
    print("Triangle is scalene")
