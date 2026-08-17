#Q7 write a program to create a dictionary and demonstrate methods and iteration.
students={101:"Kaif",102:"Aman",103:"Lalit",104:"Kartik"}
print("Itrate on Dictionary".center(50,'-'))
for id,name in students.items():
      print(f"ID : {id} Name : {name}")

print("Methods".center(50,"-"))

#assigning the copy of dictionary
#if any change happens in std_2 ,that will not affect on students
std_2=students.copy()
print("Copy of the students : ",std_2)

#Return Value of specific key

print(f"Name : {students.get(103)}")

#Update value:

students.update({102:"Shivam"})

#remove elements and return deleted element:

print(students.pop(102))


