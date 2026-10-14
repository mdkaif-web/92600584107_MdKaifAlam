#Write a program to demonstrate basic regular expression patter matching
import re
text="My name is Kaif and my GR number is 150521"
#search for a word

result=re.search("Kaif",text)
if result:
    print("Pattern found:",result.group())
else:
    print("Pattern Not Found!")
#Find all digits
numbers=re.findall(r"\d+",text)
if numbers:
    print("Numbers found : ",numbers)
else:
    print("Numbers not found!")
result_2=re.match("My",text)
if result_2:
    print("Text starts with : ",result_2.group())
else:
    print("no match found at the beginning")