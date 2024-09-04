#multiple arguments

def print_mul(*args):
    # print(args[1])
    for i in args:
        print (i)


print_mul("test","4",3)