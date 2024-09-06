#lambda

#def po(n):
#    return n**n

t=int(input("Enter the number for which the power needs to be calculated\n"))
result=lambda t:t**t
#result=po(t)
print(result(t))


a=int(input("Enter the 1st number\n"))
b=int(input("Enter the 2nd number\n"))
res=lambda a,b:a*b
print(res(a,b))

summ= lambda a,b,c:a+b+c
print(summ(10,2,3))


check_even_odd= lambda num: "even" if num%2 ==0 else "odd"
print(check_even_odd(a))
