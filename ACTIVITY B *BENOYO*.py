#default value
def hello(x = 20, y = 60, z = 40):
    print(x+y+z)

hello()

#explicit assignment of parameters
def hello(x, y = 60, z = 40):
    print(x+y+z)

hello(20)

#explicit assignment of parameters
def hello(x,y,z):
    print(x+y+z)

hello(20,60,40)


