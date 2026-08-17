#Q8 write a program to explain  mutable and immutable:

num=[12,13,14,15,16]
num_2=(20,30,40,50,60)

print("Mutable".center(50,'-'))

#it will shrink:
num.remove(15)
print(num)

#it will grow:
num.append(30)
print(num)

print("immutablity".center(50,'-'))

try:
    #whenever i want change somthing after creating immutable objec it will through error.
    #immutable object has fixed sized memory therfore it cannot be shrink,grow or update.
    num_2[5]=12
except Exception as ex:
    print(ex)


