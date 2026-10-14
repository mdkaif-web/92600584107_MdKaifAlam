import re
text="Python is easy. Python is powerful. My roll number is 4107"
# match
result1=re.match("Python",text)
print("Match: ",result1.group() if result1 else "Not found")

#search
result2=re.search("easy",text)
print("Search : ",result2.group() if result2 else "Not Found")

#findall
result3=re.findall("Python",text)
print("Findall : ",result3)