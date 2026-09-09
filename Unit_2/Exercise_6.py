nums=[20,30,40,50,60,70,80]

print("Itrating on list")

for num in nums:
    print(num,end=" ")

print()
print("Itrating on strings")

collage="Marwadi University"
for char in collage:
    print(char)
print()

print("Itrating on Dictionary")
students=[
    {"Name":"Kaif","Roll":92600584107,"Stream":"MCA","Batch":"2026-2028"},
    {"Name":"Ravi","Roll":92600584089,"Stream":"MCA","Batch":"2026-2028"}
    ]
for student in students:
    for key,value in student.items():
        print(f"{key} : {value}")
    print()


