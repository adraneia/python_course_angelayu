#unlimited positional arguements

def add(*args):
    sum = 0

    print(args[0])
    print(type(args))
    for n in args:
        sum+=n
        print(n)
    return sum

print(add(3,5,6))


print("------------calculate 1-------------")
#key word arguements
def calculate(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key)
        print(value)
    print(kwargs["add"])

calculate(add=3, multiply=5)

print("----------calculate 2---------------")

def calculate2(n, **kwargs):
    n +=kwargs["add"]
    n*= kwargs["multiply"]
    print(n)

calculate2(2, add=3, multiply=5)

print("----------my car---------------")

class Car:
    def __init__(self, **kw):
        self.make =kw["make"]
        self.model =kw["model"]

#kw = optional keyword arguements
my_car=Car(make="Nissan", model="GT-R")
print(my_car.model)


print("----------my car 222222---------------")

class Car2:
    def __init__(self, **kw):
        self.make =kw.get("make")
        self.model =kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")

#kw = optional keyword arguements
my_car=Car2(make="Nissan")
print(my_car.model)

#*args = tuple form  (1,2,3)
#**kwars = dictionary form {'x':10, 'y':64}