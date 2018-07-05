#appending first name and last name
name=str(input("enter the first name"))
surname=str(input("enter the last name"))
#no such function to append the string, but simply it can be done this way
name=name +" "+ surname
print(name)
#using %s we can use to in cur the values to print
z="%s is son of Mr. %s"%(name,surname)
print(z)
#printing using the operator
print ("{} is son of Mrs.{}".format(name,surname))