#wrapper

def decorate(a):
    print("take out the vessel and vegetables")
    print("switch on the gas")
    a()
    print("switch off the gas and the meal is ready")
    return a

@decorate
def cooking():
    print("Cook the food")
