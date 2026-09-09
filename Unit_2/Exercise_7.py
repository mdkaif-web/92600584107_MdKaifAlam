#Write a program to demonstrate list dictionary and set comprehensions
print("List Comprehension")

even=[x for x in range(1,10) if x % 2 == 0]
print(even)

print("Dictionary Comprehension")

square={x:x**2 for x in range(2,10)}
print(square)

print("Square Set")

square_set={x**2 for x in range (1,6)}
print(square_set)