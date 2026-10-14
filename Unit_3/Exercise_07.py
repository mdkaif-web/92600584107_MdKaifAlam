#Write a program to copy move and delete file using shutil module
import os
import shutil

#creating demo file for copy and move
with open("demo.txt","w") as f:
    f.write("This is a demo file") 

# Copy the File
shutil.copy("demo.txt","copy.txt")

with open("copy.txt","r") as f:
    data=f.readlines()
for row in data:
    print(row)
# move to the new folder
os.makedirs("myfolder",exist_ok=True)
shutil.move("copy.txt","myfolder/copy.txt")

#Delete the moved file 
os.remove("myfolder/copy.txt")
 