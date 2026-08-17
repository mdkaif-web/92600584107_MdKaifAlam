num_1=int(input("Enter  1st Value  "))
num_2=int(input("Enter 2nd Value  "))

try:
    print("Arithmetic Operator ".center(50,'-'))
    print(f"Addition  :{num_1+num_2}")
    print(f"Substraction :{num_1 + num_2}")
    print(f"Division   :  {num_1/num_2}")
    print(f"Multipulication  : {num_1 * num_2}")
    print(f"Remainder of Division : {num_1 % num_2}")
except ZeroDivisionError as obj:
    print(obj)

print("Relational Operator".center(50,'-'))
print("\n")

print(f" Less than  : {num_1 < num_2}")
print(f"Greater than : {num_1 > num_2 }")
print(f"Lessthan equal to : {num_1 < =num_2}")
print(f"Greaterthan equal to : {nuum_1 >=num_2}")
print(f"Equal or Not  : {num_1 == num_2}")
print("\n")

print("Logical Operator".center(50,'-'))

print('\n')

print(f" all condition are true : {num_1 < num_2 and num_1< 0}")
print(f"Anyone condition are true :{num_1 < num_2 or num_1 < 0}")




