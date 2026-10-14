#Write a program to perform file and directory operations using os and sys modules
import os 
import sys

#Current working Directory
print(f"Current Directory : {os.getcwd()}")

#Create directory
os.makedirs("Practical",exist_ok=True)

#Create a file inside the directory
file_path=os.path.join("Practical","demo.txt")

with open(file_path,"w") as f:
    f.write("This is demo file")

#List of files and directories
print(f"Directory Content : {os.listdir("Practical")}")

#Display python version using sys
print("Python Version : ",sys.version)

#Display Command Line arguments
print("Command Line Arguments : ",sys.argv)