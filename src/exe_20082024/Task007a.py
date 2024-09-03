## leap year simplified


CY=int(input("Enter the year\n"))
if (CY %4 == 0 and CY %100 != 0) or (CY %400 == 0):
    print(CY,"is a leap year")
else:
    print(CY, "is a not a leap year")
