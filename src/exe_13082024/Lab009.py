number=3.178934
format_num=(f"{number:.5f}")
print(format_num)

Appelle="shanaya"
print(type(Appelle))
print(Appelle.upper())
print(Appelle.lower())
print(len(Appelle))
Appelle=Appelle+"Mijith"
Appelle=Appelle+str(1)
print(Appelle)

Name1="Ayansh"
Name2='Mijith'
Name=Name1+Name2
print(Name)
print(Name1)

Line1="This is the first line with double quotes"
Line2='This is the second line with single quotes'
print(Line1)
print(Line2)

print(Line1,"concatenated with",Line2)
print(Line1+Line2,"concatenate using comma")
print(Line1+Line2+"concatenate using +")

age=19
agenext=19
print(id(age))
print(id(agenext))

a=["test","test2","test3"]
print(a)
b=["test","test2","test3",123456]
print(b)
print(b[0])
print(b[3])

a1=(123,345,123)
print(a1)
b1=(123,345,123, "testing")
print(b1)
print(b1[2])

d={1:"first case",2:"second case","check":891}
print(d["check"])