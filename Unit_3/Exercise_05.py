#write a program to display current date and time using datetime module.
import datetime as dt
print(f"Current Date : {dt.date.today()}")
print(f"Current Time : {dt.datetime.now().time()}")