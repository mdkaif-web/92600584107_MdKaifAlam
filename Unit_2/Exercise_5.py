#Write a program to demonstrate the use of break continue and pass statements.

orders=[
    {"id":101,"status":"completed"},
    {"id":102,"status":"cancelled"},
    {"id":103,"status":"pending"},
    {"id":104,"status":"completed"},
    {"id":105,"status":"failed"},
    {"id":106,"status":"completed"}
    ]
for order in orders:
    if order["status"] == "cancelled":
        continue
    elif order["status"] == "pending":
        pass
    elif order["status"] == "failed":
        print("Critical error.Stopping order processing")
        break
    else:
        print("Processing order :",order["id"])