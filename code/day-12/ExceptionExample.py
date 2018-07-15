s=str(input("enter a string"))
i=int(input("enter a integer"))

try:
    z=s+i
except TypeError:
    print("string and integer cannot be added")
else:
    print(z)