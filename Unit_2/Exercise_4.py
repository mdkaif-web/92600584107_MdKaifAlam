#4.Write a program find the sum of digits of a number using while loop.

num=int(input("Enter a number : "))

result=0
while num:
    temp=num % 10
    result +=temp
    num=num//10
print(f"Sum of digit is : {result}")
    
    
    
