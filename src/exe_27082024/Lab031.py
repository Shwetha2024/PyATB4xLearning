#time calculator
import time

def deco(t):
    def wrapper():
        print("start time of the test")
        a=time.time()
        print(a)
        time.sleep(4)
        t()
        print("end time of the test")
        b = time.time()
        print(b)
        print("Time taken for the test is",b-a)
    return wrapper()

@deco
def execution_time():
    print ("test run")



