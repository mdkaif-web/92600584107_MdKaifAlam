#Write a program to extract specific information from a text file using regular expressions
import re
with open("demo.txt","w") as f:
    f.write("Name: Kaif\n")
    f.write("Roll No: 4107\n")
    f.write("Email: kaif@gmail.com")

with open("demo.txt","r") as f:
    text=f.read()

#Extracting information using regular expression
name=re.search(r"Name:\s*(.*)",text)
roll=re.search(r"Roll No:\s*(\d+)",text)
email=re.search(r"Email:\s*(\S+)",text)

#Displaying Extracting information
print(f"Name: {name.group(1)}")
print(f"Roll : {roll.group(1)}")
print(f"Email : {email.group(1)}")














