from datetime import date
a=input("username:")
db={"kanish kumar":"2005","tharun":"2005","vinay":"2003","charan":"333","velluri":"234"}
while(a not in db.keys()):
    print("invalid  user")
    a=input("username:")
b=input("password:")
while not(db[a]==b):
    print("wrong password")
    b=input("password:")

print("welcome ",end=" "+a+"\n")
print("date:")
print(date.today())
