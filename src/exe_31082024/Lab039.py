#class

class dog:
    name=None
    breed=None
    color=None

    def walk(self):
        print("Walking")

    def bark(self):
        print("Barking")

dog1=dog()
print (dog1.name)
dog1.name="Bruno"
print (dog1.name)
dog1.bark()

dog2=dog()
print(dog2.name)
dog2.name="Ron"
print (dog2.name)
dog2.walk()
