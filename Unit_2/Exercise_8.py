#Write a program to illustrate variable scope using local global and nonlocal keywords
print("Variable Scope Demonstration")

x=20

def outer():
    y=20
    def inner():
        nonlocal y
        global x
        z=50 #Local variable
        print("Global Variable : ",x)
        print("Nonlocal Variable : ",y)
        print("Local Variable : ",z)

        y= x + z
        x= z + y

    inner()
    print("After inner function:")
    print("Nonlocal y : ",y)
    print("Global x   : ",x)

outer()    
