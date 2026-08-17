#Q4 write a program to demonstrate the string operation including slicing formating  and built in string functions

string=input("Enter String Values :  ")
print("String Slicing".center(50,'='))
slicing=string[1:len(string):2]# start from 2nd index to last index steps=2
print(slicing)

print("String Fromating".center(50,'='))

name='Kaif'
print('Hello' + name) # string concatination

# f string (commonly used string formating method
print(f'Hello {name}')
    
print("Built in string Functions ".center(50,'='))

#convert string into capital case
print(string.upper())

#convert into lower case
print(string.lower())

#1st lketter will be capital
print(string.title())

# check, numerical value is present or not . it will return True or False.
print(string.isdigit())

#count frequency
print(string.count('i'))

#covert string into list
print(string.split(' '))

      
