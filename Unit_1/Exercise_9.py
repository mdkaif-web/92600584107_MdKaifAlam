#Q9 write a program to define and user def-defined functions with different types of arguments

def calculate_area(length,width):
    return length * width
#default argument
def greet_user(name,city='Rajkot'):
    print(f"Name : {name} City : {city}")
#dynamic parameter:
def sum_all(*numbers):
    return sum(numbers)

print("Main".center(50,'-'))

#Positional argument (Order matters)
print("Positional Argument".center(50))

area=calculate_area(5,3)
print(f"Area of given value is : {area}")

#Keyword argument (order doesn't matter):
print("Keyword Argument".center(50))
area=calculate_area(width=20,length=10)
print("Default value")
#greeting using default value:
greet_user("Aman")

#overriding the default value:
greet_user("Kaif","Saharsa")


#Dynamic Parameters:
print("Dynamic Parameters".center(50))

result=sum_all(20,30,40,50)
print(result)
      




