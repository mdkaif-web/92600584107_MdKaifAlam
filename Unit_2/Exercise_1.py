#Write a program to demostrate conditional statements if-else and if-elif-else.

#Independent if-else.
print("if-else")
#When we have only two ways yes or no,then we use if-else
#for instance Checking a number is even or odd
nums=int(input("Enter a number : "))

if nums % 2 == 0:
    print(f"Number {nums} is even")
else:
    print(f"Number {nums} is odd")

#if-elif ladder
print("if-elif-else")

#When I have multiple ways which are connected to each other,I use if-elif ladder instead of independent if-else
#For example assigns grade based on score.

score=90

if score > 90:

    print('Grade : A')

elif  score > 70 and score <=90:

    print('Grade : B')
else:

    print('Grade : C')

