#factorial using for loop

num=int(input("Enter the number for factorial\n"))
fact=1
if num ==0 or num==1:
    fact=1
else:
    for i in range(1,num+1,1):
        fact=fact*i
print(fact)
