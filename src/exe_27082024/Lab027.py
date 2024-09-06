#global vriables


g_variable= 'globalvariable'


def local_func():
    b="localvariable"
    g_variable='localtest'
    print(g_variable)
    print(b)

def local_func_2():
    print (g_variable)
    #print(b)


local_func()
local_func_2()
print(g_variable)
#print(b)


