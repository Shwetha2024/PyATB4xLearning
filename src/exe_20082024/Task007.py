'''Leap Year Checker:

Create a program that determines whether a given year is a leap year.

A leap year is divisible by 4, but not by 100 unless it is also divisible by 400.

Use an if-else statement to make this determination.'''


# N1=input the year
# if N1%4 !=0 not leap year
# elif  N1%100!=0 leap year
# elif N1%400==0 leap year
# else not leap year

Checkyear=int(input("Enter the year\n"))
if Checkyear%4 == 0:
    if Checkyear%100 == 0:
        if Checkyear%400 == 0:
            print (f"{Checkyear} is a leap year") #2400
        else:
            print(f"{Checkyear} is not a leap year") #2100
    else:
        print(f"{Checkyear} is a leap year") #2032
else:
    print(f"{Checkyear} is not leap year")#2131
