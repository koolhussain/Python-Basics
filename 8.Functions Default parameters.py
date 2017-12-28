def simple(n1, n2):
    pass
#Assign values by default and if wanna change use the below function call
def simple(n1, n2=5):
    print(n1,n2)
    pass

simple(2)
simple(2,3)

def basic_window(width, height, font='TNR',
                 bgc='w', scrollbar=True):
    print(width, height, font, bgc)

basic_window(500,300)
#functio calls with user values which dont take the deafult values provided
basic_window(500,350,'CS')
basic_window(500,350,bgc='c')
