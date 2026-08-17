#Q5.write a program to create and manipulate lists using indexing slicing and  list comprehensions.

num_list=[20,40,50,120,160,200,220]
print("Find Value Using Index".center(50,'-'))
print(num_list[3])#index of collections are start from zero so value of 4th position will be printed

print("Slicing in list".center(50,'-'))
print(num_list[2:6:1]) # (start,stop,step) start from 3rd position to less than 6th position


print("List comprehension".center(50,'-'))

num_2=[14,15,19,16,18]
even_list=[x for x in num_2 if x%2==0]
print(even_list)

