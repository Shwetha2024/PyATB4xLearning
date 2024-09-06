#inner functions

def outer_func():
    b=40
    a="hello"
    print(a,b)

    def inner_func1():
        b=35
        print("inner1",a, b)

    def inner_func2():
        a="hi"
        print("inner2", a, b)

    inner_func1()
    inner_func2()

outer_func()

