x = 6

#acessing global variable
def example():
    global x
    print(x)
    x += 6
    print(x)

example()
print(x)

#acessing global varaible through a local varaible
#modifying that variable inside the function and then return it
#and assign it to the global variable
def example_local():
    globx = x
    print(globx, x)
    globx+=5
    print(globx, x)
    return globx

x = example_local()
print(x)
    
