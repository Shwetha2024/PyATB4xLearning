# Logic building
###User i/p -> int
###o/p -> string
###if age>21 then can go else cant go***


Age=int(input("Enter your age\n"))
print (Age)
if Age>=21:
    print(f"you are allowed to go out {Age}")
else:
    print(f"You are not allowed to go out {Age}")