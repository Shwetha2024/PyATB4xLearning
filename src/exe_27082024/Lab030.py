#wrapper

def decorate1(a):
    def wrapper():
        print("decorator 1:take out the vessel and vegetables")
        print("switch on the gas")
        a()
        print("switch off the gas and the meal is ready")
    return wrapper()

def decorate2(a):
    def wrapper():
        print("decorator 2:take out the vessel and vegetables")
        print("switch on the gas")
        a()
        print("switch off the gas and the meal is ready")
    return wrapper()

@decorate1
@decorate2
def cooking():
    print("Cook the food")





