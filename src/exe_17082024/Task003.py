
#Task3



'''Explain the difference between the = operator and the == operator in Python.
'=' is a assignment operator in whihc the right hand side value is assigned to the
left side identifier whereas '==' is used for comparison '''

a = 4
b = 5
c=a
print(c)
print(c==a)
print(a == b)
print(a == a)

'''What does the ** operator do in Python, and how is it used?
'**' is used instead of the pow function'''

print(pow(a,3))
print(b**3)

'''What does the ^ operator do in Python, and in what context is it commonly used?
'^' is XOR bitwise operator which sets each bit to 1 if only one of two bits is 1 and 
0 if both bits are same'''

i=0b0111
j=0b0011
print(i^j)


