#wrapper

def decorate(a):
    def wrapper():
        print("take out the vessel and vegetables")
        print("switch on the gas")
        a()
        print("switch off the gas and the meal is ready")
    return wrapper()

def decorate2(a):
    def wrapper():
        print("take out the vessel and vegetables")
        print("switch on the gas")
        a()
        print("switch off the gas and the meal is ready")
    return wrapper()

@decorate
@decorate2
def cooking():
    print("Cook the food")



