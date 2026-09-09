# write a program to demonstrate itrators and intrables in python

nums=[40,50,80,90,100]
#List is an itrable
print(f"Itrable : {nums}")

#Convert itrable into and itrator
itrator=iter(nums)

print("Itrator values:")

print(next(itrator))
print(next(itrator))
print(next(itrator))
print(next(itrator))
print(next(itrator))
