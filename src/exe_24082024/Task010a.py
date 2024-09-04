#factorial using for while

num=int(input("Enter the number for factorial\n"))
fact=1
i=1
while i <= num:
    fact=fact*i
    i=i+1
print(fact)
