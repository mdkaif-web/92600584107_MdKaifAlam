#Q10.write a program to demonstrate recursion using factorial or fibonacci series:

def facto(num):
    if num == 1:
        return 1
    return num * facto(num-1)
print(facto(10))

